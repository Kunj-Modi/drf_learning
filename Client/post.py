import requests

endpoint = 'http://localhost:8000/employee/create_dep/'

response = requests.post(endpoint, json={'dep_id': 7, 'dep_name': 'EXTC'})

try:
    print(response.json())
except:
    print(response)
