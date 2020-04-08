import datetime
import logging
import time

from rshanker779_common.threads import RegularRunnableThread


class ExampleRunnable(RegularRunnableThread):
    def __init__(self):
        super().__init__(datetime.timedelta(seconds=5), daemon=True)

    def do_task(self, *args, **kwargs):
        return print("Time: {}, running".format(datetime.datetime.now()))


class ErrorRunnable(RegularRunnableThread):
    def do_task(self) -> None:
        raise ValueError


def test_thread(capfd):
    r = ExampleRunnable()
    out, err = capfd.readouterr()
    assert "running" in out
    r.stop_running()


def test_error_thread(caplog):
    # with caplog.at_level(logging.ERROR):
    r = ErrorRunnable(datetime.timedelta(microseconds=1), daemon=True)
    time.sleep(0.001)
    print(caplog.messages)
    assert len(caplog.messages) == 1
    assert "Error calling do_task" in caplog.messages[0]
