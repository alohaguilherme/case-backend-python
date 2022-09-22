import unittest
from unittest.mock import Mock
from typing import List
from dataclasses import is_dataclass
from words.application.words import GroupWords, Word

response_type = List[str]


class TestWords(unittest.TestCase):

    def test_should_be_instance_isequal_dataclass(self):
        self.assertTrue(is_dataclass(GroupWords))

    def test__should_be_list_in_order_ascending(self):
        Mock()
        LIST_MOCK_SORTED_ASC: response_type = ["batman", "coringa", "robin"]
        WORD1 = Word('batman')
        WORD2 = Word('robin')
        WORD3 = Word('coringa')

        group_words = GroupWords(
            words=[
                WORD1.value,
                WORD2.value,
                WORD3.value,
            ]
        )

        result: response_type = group_words.sort_words(order="asc")
        self.assertListEqual(result, LIST_MOCK_SORTED_ASC)
        self.assertCountEqual(result, LIST_MOCK_SORTED_ASC)

    def test__should_be_list_in_order_descending(self):
        LIST_MOCK_SORTED_DESC: response_type = ['robin', 'coringa', 'batman']
        WORD1 = Word('batman')
        WORD2 = Word('robin')
        WORD3 = Word('coringa')
        group_words = GroupWords(
            words=[
                WORD1.value,
                WORD2.value,
                WORD3.value,
            ]
        )

        result: response_type = group_words.sort_words(order="desc")
        self.assertListEqual(result, LIST_MOCK_SORTED_DESC)
        self.assertCountEqual(result, LIST_MOCK_SORTED_DESC)
