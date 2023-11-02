import requests

endpoint = 'http://localhost:8000/employee/emp/1'

response = requests.get(endpoint)

print(response.json())
