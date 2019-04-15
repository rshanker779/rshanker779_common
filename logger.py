import logging


def get_logger(level: int = logging.DEBUG) -> logging.Logger:
    logging.basicConfig(level=level)
    logger = logging.getLogger(__name__)
    logger.addHandler(get_sys_out_handler())
    return logger


def get_default_formatter() -> logging.Formatter:
    return logging.Formatter('%(asctime)s - %(funcName)s - %(levelno)s - %(levelname)s - %(message)s')


def get_sys_out_handler() -> logging.Handler:
    handler = logging.StreamHandler()
    handler.setFormatter(get_default_formatter())
    return handler


def clear_handlers(logger: logging.Logger):
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)


if __name__ == '__main__':
    lgr = get_logger()
