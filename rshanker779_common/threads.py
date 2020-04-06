import datetime
import logging
import threading
import abc
from typing import Hashable, Optional, Any, Set
import time

logger = logging.getLogger(__name__)


class RegularRunnableThread(threading.Thread, abc.ABC):
    _process_map: Set[Hashable] = set()

    def __init__(
        self,
        interval: datetime.timedelta,
        daemon: bool = False,
        error_delay: datetime.timedelta = datetime.timedelta(seconds=5),
    ):
        abc.ABC.__init__(self)
        threading.Thread.__init__(self)

        self.daemon = daemon
        self.interval = interval
        self.last_run_time: Optional[datetime.datetime] = None

        self.error_delay = error_delay

        self.process_id = None
        self.stop = False
        self.start()

    def run(self) -> None:
        while True:
            try:
                if self.stop:
                    break
                now = datetime.datetime.now()
                if (
                    self.last_run_time is None
                    or now - self.last_run_time > self.interval
                ):
                    self.do_task()
                    self.last_run_time = now
            except Exception:
                logging.exception("An error occurred")
                time.sleep(self.error_delay.total_seconds())

    def ensure_single_process(self, unique_id: Optional[Hashable] = None):
        process_name = unique_id if unique_id is not None else self.__class__.__name__
        if process_name in self._process_map:
            raise threading.ThreadError(
                "Only one thread is allowed to run for this process"
            )
        else:
            self._process_map.add(process_name)

    def stop_running(self):
        self.stop = True

    @abc.abstractmethod
    def do_task(self) -> None:
        pass