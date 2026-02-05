import requests
import pytest

url_get ='https://postman-echo.com/get'
url_post='https://postman-echo.com/post'

payload = "Hi World!"
headers = {
    'postman-token': '764e0dd6-9721-4c7d-94e3-c0f270bafaa5',
    'Content-Type': 'application/json',
    'Date': '05.02.2026'
}
response_get = requests.get(url_get, headers=headers, data=payload)
response_post = requests.post(url_post, headers=headers, data=payload)

def test_response_200():
    assert  response_post.status_code == 200 and response_get.status_code == 200

def test_postman_token_valid():
    assert response_post.json()['headers']['postman-token'] == '764e0dd6-9721-4c7d-94e3-c0f270bafaa5'

def test_method_of_request_get():
    assert requests.get(url_post).status_code == 404

def test_method_of_request_post():
    assert requests.post(url_get).status_code == 404

def test_payload_post():
    assert response_post.json()['data'] == "Hi World!"

