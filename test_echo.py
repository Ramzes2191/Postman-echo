import requests

url_get ='https://postman-echo.com/get'
url_post='https://postman-echo.com/post'
headers = {
    'host': 'postman-echo.com'
}

response = requests.get(url_get, headers=headers)
print(response.json())
response = requests.post(url_post, headers=headers)
print(response.json())