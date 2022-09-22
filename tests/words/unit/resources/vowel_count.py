import unittest
from words.resources.sort import valid_fields


class TestVowelCount(unittest.TestCase):

    def test_shoud_return_dict_code_message_errror_from_word_field(self):
        response = valid_fields({})
        assert response.get('code') == 500
        assert response.get('message') == 'Words is required'
