from typing import Dict, List
from flask import Flask, request, jsonify, abort
from werkzeug.exceptions import MethodNotAllowed, NotFound
from flask_restful import Api
from words.resources import Sort, VowelCount
from infra.http import errors, validate_request
from words.application.words import Word, GroupWords


app = Flask(__name__)
api = Api(errors=errors)

api.add_resource(Sort, '/sort')
api.add_resource(VowelCount, '/vowel_count')

api.init_app(app)


@app.route("/")
def teste():
    return 'ok', 200


@app.errorhandler(NotFound)
def not_found(arguments):
    return jsonify({
        'status': 404,
        'message': "Route not exists"
    }), 404


if __name__ == "__main__":
    app.run()
