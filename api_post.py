import requests
import json

url = "https://jsonplaceholder.typicode.com/todos"
headers = {'Content-Type': 'application/json'}

data = {
"userId": 1, 
"title": "Buy groceries", 
"completed": False
}

response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.text)
