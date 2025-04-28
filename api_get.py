import requests
import json

url = "https://jsonplaceholder.typicode.com/todos"
data = requests.get(url)
print(data.status_code)
output = data.json()
print(json.dumps(output, indent =2))

