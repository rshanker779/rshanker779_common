from rshanker779_common.system import System


def test_system_hostname():
    assert isinstance(System.HOSTNAME, str)


def test_system_username():
    assert isinstance(System.USERNAME, str)


def test_platform():
    assert isinstance(System.PLATFORM, str)
