import requests

BASE = "http://127.0.0.1:5000"
user = "/api/user/"
users = "/api/users"
rooms = "/api/rooms"
room = "/api/room/"


def register_user(username, password):  # /api/users
    register = {'username': username, 'password': password}
    print("------------------------------------------------------------")
    print("register bot - USERS POST-method:")
    response = requests.post(f"{BASE}{users}", register)
    user_ID = response.json()
    print(f"registered a new user with id: {user_ID}")
    return user_ID


def create_chatroom(roomname, user_id):  # /api/rooms
    create_room = {"roomname": roomname, "creator": user_id}
    print("------------------------------------------------------------")
    print("creating a chat room - ROOMS POST-method:")
    response = requests.post(f"{BASE}{rooms}", create_room)
    room_id = response.json()
    print(f"new room created with id: {room_id}")
    return room_id


def join_chatroom(user_id, room_id):  # /api/room/<int:room_id>/users
    print("------------------------------------------------------------")
    print("joining the chat-room - MEMBERS POST-method:")
    response = requests.post(f"{BASE}{room}{room_id}/members", {'room_id': room_id, 'user_id': user_id})
    print(response.json())


def delete_chatroom(room_id):  # /api/room/<int:room_id>
    print("------------------------------------------------------------")
    print("creator of chat-room closing it - ROOMS DELETE-method:")
    response = requests.delete(
        f"{BASE}{room}{room_id}")  # (make sure to somehow verify it's the creator of the room calling this method)
    print(f"room nr {room_id} deleted: {response}")


def leave_all_members_chatroom(user_id, room_id):  # /api/room/<int:room_id>/<int:user_id>
    print("------------------------------------------------------------")
    print("leaving the chat-room - MEMBERS PUT-method:")
    response = requests.put(f"{BASE}{room}{room_id}/members")\
        # , {"user_id": user_id}  # check if creator
    print(response)


def get_all_members_chatroom(user_id, room_id):
    print("------------------------------------------------------------")
    print("get all members in chat-room - MEMBERS GET-method:")
    response = requests.get(f"{BASE}{room}{room_id}/members", {"user_id": user_id})
    print(f"members in room {room_id}{response.json()}")


usr_id1 = register_user('alex', 'password')
usr_id2 = register_user('josh', 'passsss')
usr_id3 = register_user('julia', 'lol')
usr_id4 = register_user('huzeyfe', 'bluuu')


rm_id1 = create_chatroom('datatorget', usr_id1)
rm_id2 = create_chatroom('P32', usr_id4)

join_chatroom(usr_id1, rm_id1)
join_chatroom(usr_id2, rm_id1)
join_chatroom(usr_id3, rm_id2)
join_chatroom(usr_id4, rm_id2)

get_all_members_chatroom(usr_id1, rm_id1)
get_all_members_chatroom(usr_id4, rm_id2)

# leave_all_members_chatroom(usr_id1, rm_id1)


