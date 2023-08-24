import requests

headers = {
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
}

params = {
    'invoice_id': '1',
    'callback_url': 'http://localhost:8081',
}

response = requests.post('http://localhost:8082/ocr', params=params, headers=headers)
print(response.json())