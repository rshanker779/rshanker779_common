import logging
def get_logger(level):
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)