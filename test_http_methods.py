import requests

BASE = "http://127.0.0.1:5000"
user = "/api/user/"
users = "/api/users"
user_id1 = 1
user_id2 = 2
json_user1 = {"username": "alex", "password": "password123"}
json_user2 = {"username": "josh", "password": "password456"}

# Testing Class USERS

# POST
print("------------------------------------------------------------")
print("testing USERS POST-method 1:")
response = requests.post(f"{BASE}{users}", json_user1)
print(response.json())
print("testing USERS POST-method 2:")
response = requests.post(f"{BASE}{users}", json_user2)
print(response.json())

# GET ALL
print("------------------------------------------------------------")
print("testing USERS GET-method:")
response = requests.get(f"{BASE}{users}")
print(response.json())

# Testing Class USER

# GET
print("------------------------------------------------------------")
print("testing USER GET-method:")
response = requests.get(f"{BASE}{user}{user_id2}")
print(response.json())
# DELETE
print("------------------------------------------------------------")
print("testing USER DELETE-method:")
response = requests.delete(f"{BASE}{user}{user_id1}")
print(response)


#Ufullstendig test for meldinger
print("TEST MESSAGE...")
response = requests.post(BASE + "/api/messages", {"message": "hei"})
print(response.json())
print("------------------------------------------------------------")
response = requests.get(BASE + "/api/messages")
print(response.json())