import requests

BASE = "http://127.0.0.1:5000"
user = "/api/user/"
users = "/api/users"
user_id1 = 1
user_id2 = 2
json_user1 = {"username": "alex", "password": "password123"}
json_user2 = {"username": "josh", "password": "password456"}
rooms = "/api/rooms"
room = "/api/room/"
msgPack = {"user_id": 1, "username": "uzi", "message": "heisann"}
msgPack2 = {"user_id": 2, "username": "josh", "message": "heihei"}

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
# print("------------------------------------------------------------")
# print("testing USER DELETE-method:")
# response = requests.delete(f"{BASE}{user}{user_id1}")
# print(response)


#Ufullstendig test for meldinger
# print("TEST MESSAGE...")
# response = requests.post(BASE + "/api/messages", {"message": "hei"})
# print(response.json())
# print("------------------------------------------------------------")
# response = requests.get(BASE + "/api/messages")
# print(response.json())


# TESTER ROOMS

print("------------------------------------------------------------")
print("testing ROOMS POST")
response = requests.post(f"{BASE}{rooms}", {"roomname": "nyChat", "creator": 1})
print(response.json())
print("testing ROOMS POST 2")
response = requests.post(f"{BASE}{rooms}", {"roomname": "chatNr2"})
print(response.json())

print("------------------------------------------------------------")
print("testing ROOMS GET")
response = requests.get(f"{BASE}{rooms}")
print(response.json())

print("------------------------------------------------------------")
print("testing ROOM GET <room1>")
response = requests.get(f"{BASE}{room}" + "1")
print(response.json())

# print("------------------------------------------------------------")
# print("testing ROOOM DELETE  <room2>")
# response = requests.delete(f"{BASE}{room}" + "2")
# print(response)


print("------------------------------------------------------------")
print("testing MEMBERS POST to room 1")
response = requests.post(f"{BASE}{room}{1}/{1}")
print(response.json())

print("------------------------------------------------------------")
print("testing MEMBERS POST to room 1")
response = requests.post(f"{BASE}{room}{1}/{2}")
print(response.json())

print("------------------------------------------------------------")
print("testing MEMBERS POST to room 1")
response = requests.post(f"{BASE}{room}{1}/{1}")
print(response.json())

print("------------------------------------------------------------")
print("testing MEMBERS GET member 1 from room 1")
response = requests.get(f"{BASE}{room}{1}/{1}")
print(response.json())

print("------------------------------------------------------------")
print("testing MEMBERS GET ")
response = requests.get(f"{BASE}{room}{1}/members")
print(response.json())

# TEST FOR MESSAGE

print("------------------------------------------------------------")
print("TEST MESSAGE...")
print("testing to get all messages from a room")
response = requests.get(f"{BASE}{room}/{1}/messages")
print(response.json())
print("------------------------------------------------------------")
print("testing POST message")
response = requests.post(f"{BASE}{room}{1}/{1}/messages", msgPack)
print(response.json())
print("------------------------------------------------------------")
print("testing GET message (to users who joined a room)")
response = requests.get(f"{BASE}{room}{1}/{1}/messages")
print(response.json())
print("testing GET message (from a user who isnt in the room: fail)")
response = requests.get(f"{BASE}{room}{1}/{7}/messages")
print(response.json())




