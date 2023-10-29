import requests

endpoint = 'http://localhost:8000/'

response = requests.get(endpoint, params={'abc': 1234}, json={'name': 'kunj', 'code': 1234})

print(response.json())
