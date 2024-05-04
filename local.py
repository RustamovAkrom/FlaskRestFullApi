import requests


# response = requests.post("http://127.0.0.1:3000/api/courses/3", json={"name":"JavaScript", "videos":12})
response = requests.put("http://127.0.0.1:3000/api/courses/3", json={"name": "Galang", "videos": 10})
# response = requests.delete("http://127.0.0.1:3000/api/courses/1")
print(response.json())