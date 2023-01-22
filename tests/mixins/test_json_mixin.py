import datetime
import json

from rshanker779_common.mixins import JSONMixin


class InnerNested(JSONMixin):
    def __init__(self):
        self.a = 1


class B(JSONMixin):
    def __init__(self):
        self.a = InnerNested()
        self.b = (1, 2, 3)


class HiddenAttributeC(JSONMixin):
    def __init__(self):
        self._a = 1
        self.b = 2


class DatetimeD(JSONMixin):
    def __init__(self):
        self.a = datetime.timedelta(days=1, seconds=2, milliseconds=3)


def test_json_mixin(A):
    res = json.loads(A(3).to_json())
    assert res == {"b": 3, "d": "a", "e": [1, 2, 3]}


def test_nested_classes():
    res = json.loads(B().to_json())
    assert res == {"b": [1, 2, 3], "a": {"InnerNested": {"a": 1}}}


def test_hidden_attributes():
    res = json.loads(HiddenAttributeC().to_json())
    assert res == {"b": 2}


def test_datetime():
    res = json.loads(DatetimeD().to_json())
    assert res == {"a": 86402.003}
