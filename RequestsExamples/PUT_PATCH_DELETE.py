import requests

url = 'https://jsonplaceholder.typicode.com/todos/15'
getResponse = requests.get(url)
print(getResponse.json())

#PUT
newItem = {'userId': 2, 'title': 'new Title', 'completed': False}
putResponse = requests.put(url,newItem)
print(putResponse.json())

#PATCH
newItemTitle = {'title': 'new Title PATCH'}
patchResponse = requests.patch(url,newItemTitle)
print(patchResponse.json())

#DELETE
deleteResponse = requests.delete(url)
print(deleteResponse.json())