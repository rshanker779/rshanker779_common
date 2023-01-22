from rshanker779_common.logger import clear_handlers, get_logger


def test_clear_handler():
    logger = get_logger(__name__)
    logger = clear_handlers(logger)
    assert not logger.handlers
