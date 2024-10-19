"""
Test interaction of logging with configuration system.
"""

import io
import logging
import re

from aittor.app.services.config import AIAppConfig
from aittor.backend.util.logging import LOG_FORMATTERS, AppLogger


# test formatting
# Would prefer to use the capfd/capsys fixture here, but it is broken
# when used with the logging module: https://github.com/pytest-dev/pytest/issue
def test_formatting():
    logger = AppLogger.get_logger()
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    handler.setFormatter(LOG_FORMATTERS["plain"]())
    logger.addHandler(handler)
    logger.info("test1")
    output = stream.getvalue()
    assert re.search(r"\[Aittor\]::INFO --> test1$", output)

    handler.setFormatter(LOG_FORMATTERS["legacy"]())
    logger.info("test2")
    output = stream.getvalue()
    assert re.search(r">> test2$", output)


# test independence of two loggers with different names
def test_independence():
    logger1 = AppLogger.get_logger()
    logger2 = AppLogger.get_logger("Test")
    assert logger1.name == "Aittor"
    assert logger2.name == "Test"
    assert logger1.level == logging.INFO
    assert logger2.level == logging.INFO
    logger2.setLevel(logging.DEBUG)
    assert logger1.level == logging.INFO
    assert logger2.level == logging.DEBUG


# test that the logger is returned from two similar get_logger() calls
def test_retrieval():
    logger1 = AppLogger.get_logger()
    logger2 = AppLogger.get_logger()
    logger3 = AppLogger.get_logger("Test")
    assert logger1 == logger2
    assert logger1 != logger3


# test that the configuration is used to set the initial logging level
def test_config():
    config = AIAppConfig(log_level="debug")
    logger1 = AppLogger.get_logger("DebugTest", config=config)
    assert logger1.level == logging.DEBUG
