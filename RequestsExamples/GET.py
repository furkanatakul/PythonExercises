import requests
#GET
userId = input("Enter ID: ")
getUrl = f'https://jsonplaceholder.typicode.com/todos/{userId}'
getResponse = requests.get(getUrl)
print(getResponse.json())



