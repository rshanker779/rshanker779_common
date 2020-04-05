import os
from typing import Union
from rshanker779_common import get_logger

logger = get_logger(__name__)


def make_dirs(directory: Union[str, bytes]) -> Union[str, bytes]:
    """

    :param directory:
    :return:
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def add_init_files(filepath: Union[str, bytes]):
    """

    :param filepath:
    :return:
    """
    for root, _, files in os.walk(filepath):
        # We need an init- if we have .py files, aren't in base dir (setup.py exists) and not already one
        needs_init_file = any(i for i in files if i.endswith(".py") and i != "setup.py")
        has_init_file = any(i for i in files if i == "__init__.py")
        if needs_init_file and not has_init_file:
            logger.info("Adding init file to directory %s", root)
            with open(os.path.join(root, "__init__.py"), "w") as f:
                pass
