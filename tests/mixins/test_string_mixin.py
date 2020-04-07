import rshanker779_common as utils


class A(utils.StringMixin):
    a = 1

    def __init__(self, b):
        self.b = b
        self.d = "a"

    def c(self):
        return 3


def test_string_mixin():
    assert str(A(2)) == "<A>(b=2, d=a)"
