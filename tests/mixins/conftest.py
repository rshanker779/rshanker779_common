import pytest

from rshanker779_common.mixins import JSONMixin, EqualsMixin, StringMixin


@pytest.fixture
def A():
    class A(StringMixin, EqualsMixin, JSONMixin):
        a = 1

        def __init__(self, b):
            self.b = b
            self.d = "a"
            self.e = [1, 2, 3]

        def c(self):
            return 3

    return A
