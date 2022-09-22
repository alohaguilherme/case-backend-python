import json
from typing import Dict, Union
import pytest
from app import app as Flask


@pytest.fixture(scope="module")
def app():
    Flask.config.update({
        "TESTING": True
    })
    Flask.open_resource('words/resources/sort.py')
    return Flask


@pytest.fixture()
def client(app):
    return app.test_client()


def test_should_return_flask_app_name(app):
    assert app.name == "app"


def test_should_return_status_404_in_request_different_sort_or_vowel(app):
    client = app.test_client()
    response = client.post('/teste')
    assert response.status_code == 404


def test_should_return_status_400_body_notfound_in_sort_or_vowel(client):
    MOCK_RESPONSE_ERROR_JSON: Dict[str, Union[int, str]] = {
        'status': 400, 'message': 'Body is required'}
    MOCK_RESPONSE_TYPE = "application/json"
    response = client.post(
        '/sort',
        headers={"Content-type": "application/json"}
    )
    assert response.status_code == 400
    assert response.status == "400 BAD REQUEST"
    assert response.get_json() == MOCK_RESPONSE_ERROR_JSON
    assert response.mimetype == MOCK_RESPONSE_TYPE


def test_should_return_status_500_body_is_empty_in_sort_or_vowel(client):
    MOCK_RESPONSE_ERROR_JSON: Dict[str, Union[int, str]] = {
        'code': 500, 'message': 'Internal Server Error'}
    MOCK_RESPONSE_TYPE = "application/json"
    response = client.post(
        '/sort',
        data=json.dumps({}),
        headers={"Content-type": "application/json"}
    )
    assert response.status_code == 500
    assert response.status == "500 INTERNAL SERVER ERROR"
    assert response.get_json() == MOCK_RESPONSE_ERROR_JSON
    assert response.mimetype == MOCK_RESPONSE_TYPE


def test_should_be_return_404_from_route_nonexistent(app):
    client = app.test_client()
    response = client.get('/teste')
    MOCK_RESPONSE_JSON = {
        'message': "Route not exists",
        'status': 404,
    }

    assert response.status_code == 404
    assert response.get_json() == MOCK_RESPONSE_JSON


def test_routes_ping(app):
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    assert response.text == 'ok'


def test_should_return_response_of_vowel_route_status_405(client):
    MOCK_RESPONSE_ERROR_JSON: Dict[str, Union[int, str]] = {
        'status': 405, 'message': 'The request not accept to method'}
    MOCK_RESPONSE_TYPE = "application/json"
    response = client.get(
        '/vowel_count',
        data=json.dumps({'words': ["batman", "robin", "coringa"]}),
        headers={"Content-type": "application/json"}
    )

    assert response.status_code == 405
    assert response.status == "405 METHOD NOT ALLOWED"
    assert response.get_json() == MOCK_RESPONSE_ERROR_JSON
    assert response.mimetype == MOCK_RESPONSE_TYPE


def test_should_return_response_of_vowel_route_status_415(client):
    MOCK_RESPONSE_ERROR_JSON: Dict[str, Union[int, str]] = {
        'code': 415, 'message': 'Type not supported for app'}
    MOCK_RESPONSE_TYPE = "application/json"
    response = client.post(
        '/vowel_count',
        data=json.dumps({'words': ["batman", "robin", "coringa"]}),
    )

    assert response.status_code == 415
    assert response.status == "415 UNSUPPORTED MEDIA TYPE"
    assert response.get_json() == MOCK_RESPONSE_ERROR_JSON
    assert response.mimetype == MOCK_RESPONSE_TYPE


def test_should_return_response_of_vowel_route_status_200(client):
    response = client.post(
        '/vowel_count',
        data=json.dumps({'words': ["batman", "robin", "coringa"]}),
        headers={"Content-type": "application/json"}
    )

    assert response.status_code == 200


def test_should_return_response_total_vowels_in_word(client):
    MOCK_RESPONSE_JSON = {
        "batman": 2,
        "coringa": 3,
        "robin": 2
    }
    response = client.post(
        '/vowel_count',
        data=json.dumps({'words': ["batman", "robin", "coringa"]}),
        headers={"Content-type": "application/json"}
    )

    assert response.get_json() == MOCK_RESPONSE_JSON


def test_should_return_response_of_sort_route_status_405(client):
    MOCK_RESPONSE_ERROR_JSON: Dict[str, Union[int, str]] = {
        'status': 405, 'message': 'The request not accept to method'}
    MOCK_RESPONSE_TYPE = "application/json"
    response = client.get(
        '/sort',
        data=json.dumps(
            {'words': ["batman", "robin", "coringa"], 'order': 'asc'}),
        headers={"Content-type": "application/json"}
    )

    assert response.status_code == 405
    assert response.status == "405 METHOD NOT ALLOWED"
    assert response.get_json() == MOCK_RESPONSE_ERROR_JSON
    assert response.mimetype == MOCK_RESPONSE_TYPE


def test_should_return_response_of_sort_route_status_415(client):
    MOCK_RESPONSE_ERROR_JSON: Dict[str, Union[int, str]] = {
        'code': 415, 'message': 'Type not supported for app'}
    MOCK_RESPONSE_TYPE = "application/json"
    response = client.post(
        '/sort',
        data=json.dumps(
            {'words': ["batman", "robin", "coringa"], 'order': 'asc'}),
    )

    assert response.status_code == 415
    assert response.status == "415 UNSUPPORTED MEDIA TYPE"
    assert response.get_json() == MOCK_RESPONSE_ERROR_JSON
    assert response.mimetype == MOCK_RESPONSE_TYPE


def test_should_return_response_of_sort_route_status_200(client):
    response = client.post(
        '/sort',
        data=json.dumps(
            {'words': ["batman", "robin", "coringa"], 'order': 'asc'}),
        headers={"Content-type": "application/json"}
    )
    assert response.status_code == 200


def test_should_return_response_list_words_sorted_asc(client):
    response = client.post(
        '/sort',
        data=json.dumps(
            {'words': ["batman", "robin", "coringa"], 'order': 'asc'}),
        headers={"Content-type": "application/json"}
    )
    assert response.status_code == 200
    assert response.get_json() == ["batman", "coringa", "robin"]


def test_should_return_response_list_words_sorted_desc(client):
    response = client.post(
        '/sort',
        data=json.dumps(
            {'words': ["batman", "robin", "coringa"], 'order': 'desc'}),
        headers={"Content-type": "application/json"}
    )

    assert response.get_json() == ["robin", "coringa", "batman"]
    assert response.mimetype == "application/json"
    assert response.status == "200 OK"
