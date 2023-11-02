import requests

endpoint = 'http://localhost:8000/employee/create_emp/'

response = requests.post(endpoint, json={'emp_id': 18, 'emp_name': 'kriya', 'emp_dep': 3})

try:
    print(response.json())
except:
    print(response)
