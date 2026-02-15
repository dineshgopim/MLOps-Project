import requests
import json

url = "https://sturdy-capybara-975rvrjrxvprc95wv-5000.app.github.dev/predict"

test_data = {
    'pclass' : 1,
    'sex' : 'female',
    'age' : 38,
    'fare': 71.28,
    'parch': 0
}

responce = requests.post(url, json=test_data)

print("Status Code:", responce.status_code)
print("Raw Text Response:", responce.text)


