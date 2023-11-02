import requests

endpoint = 'http://localhost:8000/employee/create_emp/'

response = requests.post(endpoint, json={'emp_id': 15, 'emp_name': 'hitansh', 'emp_dep': 5})

try:
    print(response.json())
except:
    print(response)
