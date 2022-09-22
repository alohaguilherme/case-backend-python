from typing import Dict, List
from flask import request, jsonify, make_response
from flask_restful import Resource
from infra.http.validation import validate_request
from words.application.words import GroupWords

# types

words_list = List[str]


def valid_fields(body: Dict):
    if not body.get('words'):
        return {"code": 500, "message":  "Words is required"}
    return None


class VowelCount(Resource):
    def post(self):
        if error := validate_request(request):
            return make_response(
                jsonify({
                    'code': error.get('code'),
                    'message': error.get('message')
                }),
                error.get('code')
            )
        elif error := valid_fields(request.get_json()):
            return make_response(
                jsonify({
                    'code': error.get('code'),
                    'message': error.get('message')
                }),
                error.get('code')
            )
        words: words_list = request.get_json().get('words')
        group_words = GroupWords(words)

        return group_words.count_vowels_list()
