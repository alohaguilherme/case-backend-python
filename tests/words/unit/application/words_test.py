import unittest
from unittest.mock import Mock, patch
from dataclasses import is_dataclass
from words.application.words import Word


class TestWords(unittest.TestCase):
    WORD_MOCK: str = "batman"

    def test_should_be_instance_isequal_dataclass(self):
        self.assertTrue(is_dataclass(Word))

    def test_should_be_type_equal_string_value(self):
        word = Word(value=self.WORD_MOCK)
        self.assertIsInstance(word.value, str)

    def test_should_be_return_raise_error_in_value_None(self):
        word = Word(value=None)
        self.assertIsNone(word.value)

    def test_should_be_the_value_is_NotNone(self):
        word = Word(value=self.WORD_MOCK)
        self.assertIsNotNone(word.value)

    def test_should_be_return_total_vowels_word(self):
        word = Word(value=self.WORD_MOCK)
        self.assertEqual(word.count_vowels_in_word(), 2)
