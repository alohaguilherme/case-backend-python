from flask import Flask, jsonify
from werkzeug.exceptions import NotFound
from flask_restful import Api
from words.resources import Sort, VowelCount
from infra.http import errors


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
