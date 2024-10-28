import json

import requests

# send get request
r = requests.get("http://127.0.0.1:8000")

# print status update
print(f"Status Update: {r.status_code}")

# print welcome message
print(f"Message: {r.text}")



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# send a POST using the data above
r = requests.post("http://127.0.0.1:8000/data/", json=data)

# print status update
print(f"Status Update: {r.status_code}")

# print results message
print(f"Results: {r.json()}")
