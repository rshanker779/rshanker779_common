import rshanker779_common as utils


def test_system_hostname():
    assert isinstance(utils.System.HOSTNAME, str)


def test_system_username():
    assert isinstance(utils.System.USERNAME, str)
