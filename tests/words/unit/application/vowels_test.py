import unittest
from words.application.vowels import Vowels


class TestVowels(unittest.TestCase):

    def test_should_return_equal_to_2(self):
        WORDMOCK: str = "batman"
        count_result = Vowels.count(WORDMOCK)
        self.assertEqual(count_result, 2)
