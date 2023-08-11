import unittest
from ..utils.nickname import check_nickname

class TestNicknameValidation(unittest.TestCase):

    def test_valid_nickname(self):
        self.assertTrue(check_nickname("User123")[0])

    def test_non_ascii_nickname(self):
        self.assertFalse(check_nickname("User_èé")[0])

    def test_empty_nickname(self):
        self.assertFalse(check_nickname("")[0])

    def test_nickname_with_spaces(self):
        self.assertFalse(check_nickname("User Name")[0])

    def test_long_nickname(self):
        self.assertFalse(check_nickname("ThisIsALongNicknameThatIsInvalid")[0])

if __name__ == '__main__':
    unittest.main()
