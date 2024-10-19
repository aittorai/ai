import json
from pathlib import Path

from aittor.app.services.operator import Operator
from aittor.app.services.shared.sqlite.sqlite_database import SqliteDatabase
from aittor.app.services.style_preset_records.style_preset_records_base import StylePresetRecordsStorageBase
from aittor.app.services.style_preset_records.style_preset_records_common import (
    PresetType,
    StylePresetChanges,
    StylePresetNotFoundError,
    StylePresetRecordDTO,
    StylePresetWithoutId,
)
from aittor.app.util.misc import uuid_string


class SqliteStylePresetRecordsStorage(StylePresetRecordsStorageBase):
    def __init__(self, db: SqliteDatabase) -> None:
        super().__init__()
        self._lock = db.lock
        self._conn = db.conn
        self._cursor = self._conn.cursor()

    def start(self, operator: Operator) -> None:
        self._operator = operator
        self._sync_default_style_presets()

    def get(self, style_preset_id: str) -> StylePresetRecordDTO:
        """Gets a style preset by ID."""
        try:
            self._lock.acquire()
            self._cursor.execute(
                """--sql
                SELECT *
                FROM style_presets
                WHERE id = ?;
                """,
                (style_preset_id,),
            )
            row = self._cursor.fetchone()
            if row is None:
                raise StylePresetNotFoundError(f"Style preset with id {style_preset_id} not found")
            return StylePresetRecordDTO.from_dict(dict(row))
        except Exception:
            self._conn.rollback()
            raise
        finally:
            self._lock.release()

    def create(self, style_preset: StylePresetWithoutId) -> StylePresetRecordDTO:
        style_preset_id = uuid_string()
        try:
            self._lock.acquire()
            self._cursor.execute(
                """--sql
                INSERT OR IGNORE INTO style_presets (
                    id,
                    name,
                    preset_data,
                    type
                )
                VALUES (?, ?, ?, ?);
                """,
                (
                    style_preset_id,
                    style_preset.name,
                    style_preset.preset_data.model_dump_json(),
                    style_preset.type,
                ),
            )
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise
        finally:
            self._lock.release()
        return self.get(style_preset_id)

    def create_many(self, style_presets: list[StylePresetWithoutId]) -> None:
        style_preset_ids = []
        try:
            self._lock.acquire()
            for style_preset in style_presets:
                style_preset_id = uuid_string()
                style_preset_ids.append(style_preset_id)
                self._cursor.execute(
                    """--sql
                    INSERT OR IGNORE INTO style_presets (
                        id,
                        name,
                        preset_data,
                        type
                    )
                    VALUES (?, ?, ?, ?);
                    """,
                    (
                        style_preset_id,
                        style_preset.name,
                        style_preset.preset_data.model_dump_json(),
                        style_preset.type,
                    ),
                )
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise
        finally:
            self._lock.release()

        return None

    def update(self, style_preset_id: str, changes: StylePresetChanges) -> StylePresetRecordDTO:
        try:
            self._lock.acquire()
            # Change the name of a style preset
            if changes.name is not None:
                self._cursor.execute(
                    """--sql
                    UPDATE style_presets
                    SET name = ?
                    WHERE id = ?;
                    """,
                    (changes.name, style_preset_id),
                )

            # Change the preset data for a style preset
            if changes.preset_data is not None:
                self._cursor.execute(
                    """--sql
                    UPDATE style_presets
                    SET preset_data = ?
                    WHERE id = ?;
                    """,
                    (changes.preset_data.model_dump_json(), style_preset_id),
                )

            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise
        finally:
            self._lock.release()
        return self.get(style_preset_id)

    def delete(self, style_preset_id: str) -> None:
        try:
            self._lock.acquire()
            self._cursor.execute(
                """--sql
                DELETE from style_presets
                WHERE id = ?;
                """,
                (style_preset_id,),
            )
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise
        finally:
            self._lock.release()
        return None

    def get_many(self, type: PresetType | None = None) -> list[StylePresetRecordDTO]:
        try:
            self._lock.acquire()
            main_query = """
                SELECT
                    *
                FROM style_presets
                """

            if type is not None:
                main_query += "WHERE type = ? "

            main_query += "ORDER BY LOWER(name) ASC"

            if type is not None:
                self._cursor.execute(main_query, (type,))
            else:
                self._cursor.execute(main_query)

            rows = self._cursor.fetchall()
            style_presets = [StylePresetRecordDTO.from_dict(dict(row)) for row in rows]

            return style_presets
        except Exception:
            self._conn.rollback()
            raise
        finally:
            self._lock.release()

    def _sync_default_style_presets(self) -> None:
        """Syncs default style presets to the database. Internal use only."""

        # First delete all existing default style presets
        try:
            self._lock.acquire()
            self._cursor.execute(
                """--sql
                DELETE FROM style_presets
                WHERE type = "default";
                """
            )
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise
        finally:
            self._lock.release()
        # Next, parse and create the default style presets
        with self._lock, open(Path(__file__).parent / Path("default_style_presets.json"), "r") as file:
            presets = json.load(file)
            for preset in presets:
                style_preset = StylePresetWithoutId.model_validate(preset)
                self.create(style_preset)
