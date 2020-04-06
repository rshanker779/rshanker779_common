import rshanker779_common as utils
import pathlib
import tempfile
import os
import pytest


@pytest.fixture
def build_init_directories(tmp_path):
    (tmp_path / "setup.py").write_text("import setuptools")
    (tmp_path / "a").mkdir()
    (tmp_path / "a" / "test.py").write_text("")
    (tmp_path / "a" / "b").mkdir()
    (tmp_path / "a" / "b" / "c").mkdir()
    (tmp_path / "a" / "b" / "c" / "nested.py").write_text("")
    yield


def test_init_directories(tmpdir, build_init_directories):
    utils.add_init_files(tmpdir)
    assert not (tmpdir / "__init__.py").isfile()
    assert (tmpdir / "a" / "__init__.py").isfile()
    assert not (tmpdir / "a" / "b" / "__init__.py").isfile()
    assert (tmpdir / "a" / "b" / "c" / "__init__.py").isfile()


def test_relative_path():
    assert utils.relative_path() == pathlib.Path(__file__).parent
    assert utils.relative_path("a", "b") == pathlib.Path(__file__).parent / "a" / "b"
