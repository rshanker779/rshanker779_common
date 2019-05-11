import logging


def get_logger(level: int = logging.DEBUG) -> logging.Logger:
    logger = logging.getLogger(__name__)
    if not logger.handlers:
        logger.addHandler(get_sys_out_handler())
    logger.setLevel(level)
    return logger


def get_default_formatter() -> logging.Formatter:
    return logging.Formatter('%(asctime)s - %(funcName)s - %(levelno)s - %(levelname)s - %(message)s')


def get_sys_out_handler() -> logging.Handler:
    handler = logging.StreamHandler()
    handler.setFormatter(get_default_formatter())
    return handler


def clear_handlers(logger: logging.Logger)->logging.Logger:
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    return logger

lgr = get_logger()

if __name__ == '__main__':
    lgr = get_logger()
    lgr.info("hi")
