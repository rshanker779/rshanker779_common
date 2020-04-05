import pathlib
import pytest
import rshanker779_common as utils


@pytest.fixture
def example_function():
    def example_string_function(x, y):
        return str(reversed(x)) + y

    return example_string_function


def test_profiler(example_function):
    profiler = utils.Profiler(example_function, 100, "xfsjkfljkslf", "fkdskfl")
    profiler.profile()
    assert pathlib.Path(profiler.filename).is_file()
