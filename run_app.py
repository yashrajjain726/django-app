import requests
import json

URL = "http://localhost:8000/productApi/"


def get_product_details(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    response = requests.get(url=URL, data=json_data)
    data = response.json()
    print(data)


def post_product_details():
    data = {'id': 231, 'name': 'yash', 'measurement_unit': 'Kg'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


def update_product_details():
    data = {'id': 53, 'name': 'yashraj', 'measurement_unit': 'Kg'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


def delete_product_details():
    data = {'id': 23}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


update_product_details()
