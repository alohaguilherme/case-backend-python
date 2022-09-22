from typing import Dict
from flask import request, jsonify, make_response
from flask_restful import Resource
from infra.http.validation import validate_request
from words.application.words import GroupWords


def valid_fields(body: Dict):
    if not body.get('words'):
        return {"code": 500, "message":  "Words is required"}
    if not body.get('order'):
        return {"code": 500, "message":  "Order is required"}
    return None


class Sort(Resource):
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

        response = request.get_json()
        words = response.get('words')
        order = response.get('order')

        group_words = GroupWords(words)

        return group_words.sort_words(order=order)
