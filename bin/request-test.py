import requests
resp = requests.get('http://127.0.0.1:3000/json')
resp = resp.json()
print(resp)