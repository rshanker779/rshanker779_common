import logging
def get_logger(level=logging.DEBUG):
    logging.basicConfig(level=level)
    logger = logging.getLogger(__name__)
    return logger