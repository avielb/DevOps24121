import requests

# response = requests.delete("http://localhost:8080/items/1")
response = requests.get("http://localhost:8080/items")
a = response.json()
for i in a:
    print(i.get("name"))