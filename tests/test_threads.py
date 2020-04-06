import datetime

from rshanker779_common.threads import RegularRunnableThread


class ExampleRunnable(RegularRunnableThread):
    def __init__(self):
        super().__init__(datetime.timedelta(seconds=5), daemon=True)

    def do_task(self, *args, **kwargs):
        return print("Time: {}, running".format(datetime.datetime.now()))


def test_thread(capfd):
    r = ExampleRunnable()
    out, err = capfd.readouterr()
    assert "running" in out
    r.stop_running()
