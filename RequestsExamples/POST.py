import requests
import json

#POST
todoItem = {"userId" : 2, "title" : "my to do", "completed" : False}
postUrl = "https://jsonplaceholder.typicode.com/todos"
#optional header
headres = {"Content-Type" : "application/json"}
postResponse = requests.post(postUrl,todoItem,headres)
print(postResponse.json())
print(type(todoItem))
print(type(json.dumps(todoItem)))