from enum import Enum

from aittor.app.util.metaenum import MetaEnum

sqlite_memory = ":memory:"


class SQLiteDirection(str, Enum, metaclass=MetaEnum):
    Ascending = "ASC"
    Descending = "DESC"
