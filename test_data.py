import requests
import json

url = 'http://127.0.0.1:5000/predict'

test_data = {
    'pclass' : 1,
    'sex' : 'female',
    'age' : 38,
    'fare': 71.28,
    'parch': 0
}

responce = requests.post(url, json=test_data)

print(f"Server Responce: {responce.json()}")
