import rshanker779_common as utils
import pathlib
import tempfile

import pytest


@pytest.fixture
def build_init_directories(tmp_path):
    (tmp_path / "setup.py").write_text("import setuptools")
    (tmp_path / "a").mkdir()
    (tmp_path / "a" / "test.py").write_text("")
    (tmp_path / "a" / "b").mkdir()
    yield


def test_init_directories(tmpdir, build_init_directories):
    utils.add_init_files(tmpdir)
    assert not (tmpdir / "__init__.py").isfile()
    assert (tmpdir / "a" / "__init__.py").isfile()
    assert not (tmpdir / "a" / "b" / "__init__.py").isfile()
