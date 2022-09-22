from ast import Raise
from logging import raiseExceptions
from typing import ClassVar, Dict, List, Optional, Union
from dataclasses import dataclass
from .vowels import Vowels

# Types
word = str
order = str
list_words = List[word]
list_words_vowels = Dict[word, int]


@ dataclass()
class GroupWords:
    words: List[word]

    def count_vowels_list(self) -> list_words_vowels:
        response = {}
        for value in self.words:
            word = Word(value)
            total_vowels: int = word.count_vowels_in_word()
            response.update({word.value: total_vowels})

        return response

    def sort_words(self, order: order) -> list_words:
        return sorted(self.words, reverse=(order == "desc"))


@ dataclass()
class Word:
    value: str

    def count_vowels_in_word(self) -> int:
        result = Vowels.count(self.value)
        return result
