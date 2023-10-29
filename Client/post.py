import requests

endpoint = 'http://localhost:8000/student/add/'

response = requests.post(endpoint, json={'name': 'ved', 'age': 19, 'email': 'ved@gm.co'})

try:
    print(response.json())
except:
    print(response)
