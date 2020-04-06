import logging

import rshanker779_common as utils


@utils.time_it
def example_function():
    return 1


def test_time_it(caplog):
    with caplog.at_level(logging.INFO):
        res = example_function()
    assert res == 1
    assert len(caplog.messages) == 1
    assert "example_function executed in" in caplog.messages[0]
