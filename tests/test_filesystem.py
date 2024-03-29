import pathlib

import pytest

from rshanker779_common.filesytem import add_init_files, relative_path, make_dirs, Path


@pytest.fixture
def build_init_directories(tmp_path):
    (tmp_path / "setup.py").write_text("import setuptools")
    (tmp_path / "a").mkdir()
    (tmp_path / "a" / "test.py").write_text("")
    (tmp_path / "a" / "b").mkdir()
    (tmp_path / "a" / "b" / "c").mkdir()
    (tmp_path / "a" / "b" / "c" / "nested.py").write_text("")
    yield


def test_init_directories(tmp_path, build_init_directories):
    add_init_files(tmp_path)
    assert not (tmp_path / "__init__.py").is_file()
    assert (tmp_path / "a" / "__init__.py").is_file()
    assert not (tmp_path / "a" / "b" / "__init__.py").is_file()
    assert (tmp_path / "a" / "b" / "c" / "__init__.py").is_file()


def test_relative_path():
    assert relative_path().path == pathlib.Path(__file__).parent
    assert relative_path("a", "b").path == pathlib.Path(__file__).parent / "a" / "b"


def test_make_dirs(tmp_path):
    res = make_dirs(tmp_path / "example")
    assert (tmp_path / "example").is_dir()
    assert res.path == (tmp_path / "example")


def test_path_has_pathlib_attributes(tmp_path):
    example_path = Path(tmp_path)
    assert hasattr(example_path, "glob")
    assert not example_path.ls()
    assert isinstance(example_path / "b", Path)
    (example_path / "a.txt").write_text("a")
    assert len(example_path.ls()) == 1
    assert "glob" in dir(example_path)
