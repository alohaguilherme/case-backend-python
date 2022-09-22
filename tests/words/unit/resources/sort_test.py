import unittest
from words.resources.sort import valid_fields


class TestSort(unittest.TestCase):

    def test_shoud_return_dict_code_message_errror_from_word_field(self):
        response = valid_fields({'order': 'asc'})
        assert response.get('code') == 500
        assert response.get('message') == 'Words is required'

    def test_shoud_return_dict_code_message_errror_from_order_field(self):
        response = valid_fields({'words': ['asc']})
        assert response.get('code') == 500
        assert response.get('message') == 'Order is required'
