import getpass
import socket


class System:
    HOSTNAME = socket.gethostname()
    USERNAME = getpass.getuser()
