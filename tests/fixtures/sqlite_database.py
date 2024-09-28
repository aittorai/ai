from logging import Logger
from unittest import mock

from aittor.app.services.config.config_default import AIAppConfig
from aittor.app.services.image_files.image_files_base import ImageFileStorageBase
from aittor.app.services.shared.sqlite.sqlite_database import SqliteDatabase
from aittor.app.services.shared.sqlite.sqlite_util import init_db


def create_mock_sqlite_database(config: AIAppConfig, logger: Logger) -> SqliteDatabase:
    image_files = mock.Mock(spec=ImageFileStorageBase)
    db = init_db(config=config, logger=logger, image_files=image_files)
    return db
