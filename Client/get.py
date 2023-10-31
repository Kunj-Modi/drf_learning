import requests

endpoint = 'http://localhost:8000/getUsers/'

response = requests.get(endpoint)

print(response.json())
