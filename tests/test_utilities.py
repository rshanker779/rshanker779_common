import unittest
import rshanker779_common.utilities as utils


class UtilitiesTest(unittest.TestCase):
    def test_get_hostname(self):
        """Test no error thrown"""
        utils.get_hostname()

    def test_get_username(self):
        """Test no error thrown"""
        utils.get_username()


if __name__ == "__main__":
    unittest.main()
