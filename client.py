from nltk.chat.util import Chat, reflections
import requests


# ################################# BOTS ###################################

def julia():
    pairs = [
        (r"username", "julia"),
        (r"alias", ["jullz", "wiklund", "j****w"]),
        (r"password", ["julia123", "wiklund456"]),
        (r"roomname", ["oblig2chatt", "olafiaklinikken"]),
        (r"start conversation", ["Hi everyone, welcome to the chat", "Hey guys, nice to see you're all here"]),
        (r"bye", ["bye", "see ya"]),
        (r"(.*)ketchup(.*)", ["AAAH, elsker mackern", "Jeg liker friiies med ketchup"])
    ]
    chatbot = Chat(pairs, reflections)
    return chatbot


def alex():
    pass


def huzeyfe():
    pass


def josh():
    pass


# ################################### EXAMPLE INPUT ####################################

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


# ################################### CLIENT METHODS ####################################

def register_user(chatbot):  # /api/users
    register = {'username': chatbot.respond('username'), 'password': chatbot.respond('password')}
    print("------------------------------------------------------------")
    print("register bot - USERS POST-method:")
    response = requests.post(f"{BASE}{users}", register)
    user_ID = response.json()
    print(f"registered a new user with id: {user_ID}")
    return user_ID


def create_chatroom(chatbot, user_id):  # /api/rooms
    create_room = {"roomname": chatbot.respond('roomname'), "creator": user_id}
    print("------------------------------------------------------------")
    print("creating a chat room - ROOMS POST-method:")
    response = requests.post(f"{BASE}{rooms}", create_room)
    room_id = response.json()
    print(f"new room created with id: {room_id}")
    return room_id


def delete_chatroom(room_id):  # /api/room/<int:room_id>
    print("------------------------------------------------------------")
    print("creator of chat-room closing it - ROOMS DELETE-method:")
    response = requests.delete(
        f"{BASE}{room}{room_id}")  # (make sure to somehow verify it's the creator of the room calling this method)
    return response


def join_chatroom(user_id, room_id):  # /api/room/<int:room_id>/users
    print("------------------------------------------------------------")
    print("joining the chat-room - MEMBERS POST-method:")
    response = requests.post(f"{BASE}{room}{room_id}/{user_id}")
    print(response.json())
    return True


def start_conversation(chatbot, user_id, room_id):  # /api/room/<int:room_id>/<int:user_id>/messages
    msg = chatbot.respond("start conversation")
    alias = chatbot.respond("alias")
    msg_json = {"user_id": user_id, "username": alias, "message": msg}
    response = requests.post(f"{BASE}{room}{room_id}/{user_id}/messages", msg_json)
    print("------------------------------------------------------------")
    print("starting conversation in chat-room - MESSAGES2 POST-method:")
    msg = response.json()
    return msg


#   return response.json()


def recieve_messages(user_id, room_id):  # /api/room/<int:room_id>/<int:user_id>/messages
    response = requests.get(f"{BASE}{room}{room_id}/{user_id}/messages")
    msg = response.json()
    #    for m in msg:
    #        if m != msg[user_id]:
    #            format_and_print_msg(m)
    return msg


def format_and_print_msg(msg):
    print(f"{msg['username']} says: {msg['message']} ")


def leave_chatroom(user_id, room_id):  # /api/room/<int:room_id>/<int:user_id>
    print("------------------------------------------------------------")
    print("leaving the chat-room - MEMBERS DELETE-method:")
    response = requests.delete(f"{BASE}{room}{room_id}/{user_id}")
    print(response)
    return False

# ############################ RUNNING PROGRAM #####################################


def client_connected_to_server(chatbot):
    user_id = register_user(chatbot)
    connected = True
    while connected:
        room_id = create_chatroom(chatbot, user_id)
        in_chatroom = join_chatroom(user_id, room_id)
        msg = start_conversation(chatbot, user_id, room_id)
        format_and_print_msg(msg)
        while in_chatroom:
            #    msg = recieve_messages(user_id, room_id)
            if msg['message'] == "bye":
                in_chatroom = leave_chatroom(user_id, room_id)
            in_chatroom = False

        connected = False


bot = julia()  # starting chatbot
client_connected_to_server(bot)
