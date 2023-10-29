import requests

endpoint = 'http://localhost:8000/student'

response = requests.get(endpoint)

print(response.json())
