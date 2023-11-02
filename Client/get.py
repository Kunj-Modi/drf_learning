import requests

endpoint = 'http://localhost:8000/employee/list_emp/?p=2'

response = requests.get(endpoint)

print(response.json())
