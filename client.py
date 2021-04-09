from nltk.chat.util import Chat, reflections
import requests
import random


# ################################# BOTS ###################################

def julia():
    pairs = [
        (r"username", ["julia"]),
        (r"alias", ["jullz", "wiklund", "j****w"]),
        (r"password", ["julia123", "wiklund456"]),
        (r"roomname", ["oblig2chatt", "olafiaklinikken"]),
        (r"start conversation", ["Hi everyone, welcome to the chat", "Hey guys, nice to see you're all here"]),
        (r"choose rooom (.*)", ["0", "1", "2", "3"]),
        (r"bye", ["bye", "see ya"]),
        (r"(.*)ketchup(.*)", ["AAAH, elsker mackern", "Jeg liker friiies med ketchup"])
    ]
    chatbot = Chat(pairs, reflections)
    return chatbot


def alex():
    pairs = [
        (r"username", "alex"),
        (r"alias", ["alexxx", "ale", "alez"]),
        (r"password", ["ale123", "hvordanlagermanpassord123"]),
        (r"roomname", ["datanett gc", "the gang", "cabbage"]),
        (r"start conversation", ["Hiii girliesss, hope everybody is having a good day, welcome to the chat",
                                 "Wuddup errybody, i made this soooo lets talk",
                                 "Hello and welcome to the gc :) hope we'll have a nice convo"]),
        (r"choose rooom (.*)", ["0", "1", "2", "3"]),
        (r"bye", ["byebyeee", "ttyl bye", "tnx for today:) byeee"]),
        (r"(.*)food(.*)", ["I looooove spicy food hihi", "I could eat every day, oh wait, i already do hahah",
                           "I love to make food, i also like baking, but i dont like pastries so not a good combo"]),
        (r"(.*)sport(.*)|(.*)sports(.*)", ["Ehheh I dont really watch or play any sports anymore",
                                           "Sports? Nope not for me", "I play games, not sports"]),
        (r"(.*)movies(.*)|(.*)movie(.*)", ["I like horror movies, but there hasn't really been any good ones lately",
                                           "Lovee all of the studio ghibli movies, nostalgia u know",
                                           "I like 'Sunshine in a spotless mind' cuz it feels like a dream hehe"])
    ]
    alex_bot = Chat(pairs, reflections)
    return alex_bot


def huzeyfe():
    pairs = [
        (r"username", "Huzeyfe"),
        (r"alias", ["uzi", "huzi", "theuzi123", "phoenix", "BigBoy2k"]),
        (r"password", ["ilovevalorant123", "val_uzi2021", "mypass_secret"]),
        (r"roomname", ["Time for Val!", "Gaming room", "diskusjons toalett"]),
        (r"start conversation", ["Welcome to the gaming universe guys:)",
                                 "Heyyy bros!, long time no see. How are you?",
                                 "Bro im really sad, some one wanna talk?"]),
        (r"bye", ["See you guys later",
                  "yeah was nice to talk with you guys, hope we can do it again next week",
                  "Im out boyyyys, have to meet my girlfriend",
                  "I really appreciate the conversation, goodbye",
                  "Bye guys, we'll talk later",
                  "Goodbye!"]),
        (r"(.*)food(.*)", ["Bro cant you see that I love food? Like look at me dude!",
                           "I can really eat everything, it's starting to get a big problem",
                           "I'm not a big fan of proper food, but I can eat snacks anytime",
                           "Food?! fuck now i'm just thinking about chicken tikka masala, chicken curry, chicken tandori, chicken biryani aaaaarghh",
                           "I do not eat anything but sweets",
                           "I have anorexia, can we talk about something else?"]),
        (r"(.*)sport(.*)|(.*)sports(.*)", ["Bro I watch sports all the time!",
                                           "Sports are perhaps some of the most boring things you can do",
                                           "Bro I love sport, especially boxing",
                                           "Hahaha sport? I can 't even get out of bed, you're funny"]),
        (r"(.*)movies(.*)|(.*)movie(.*)", ["I mean everyone should have at least one movie night a week",
                                           "Yeeah I am obsessed with star wars, i know absolutely everything about it:)",
                                           "To be honest I do not like movies, I prefer series",
                                           "I'm not actually watching movies guys:/",
                                           "Ouf I love documentaries, maybe that's why everyone calls me a nerd..."]),
        # (r"(.*)feeling(.*)|(.*)feelings(.*)|(.*)feel(.*)", [])

    ]
    huzeyfe_bot = Chat(pairs, reflections)
    return huzeyfe_bot


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


def get_all_chatrooms(user_id):  # /api/rooms
    user_json = {"user_id": user_id}
    print("------------------------------------------------------------")
    print("getting all chat rooms - ROOMS GET-method:")
    response = requests.get(f"{BASE}{rooms}", user_json)
    all_chatrooms = response.json()
    format_and_print_room(all_chatrooms)
    return all_chatrooms


def choose_room(room_list):
    last_index = len(room_list['rooms']) - 1
    room_index = random.randint(0, last_index)
    return room_index


def join_chatroom(user_id, room_id):  # /api/room/<int:room_id>/users
    print("------------------------------------------------------------")
    print("joining the chat-room - MEMBERS POST-method:")
    response = requests.post(f"{BASE}{room}{room_id}/members", {'room_id': room_id, 'user_id': user_id})
    print(response.json())
    return True


def delete_chatroom(room_id):  # /api/room/<int:room_id>
    print("------------------------------------------------------------")
    print("creator of chat-room closing it - ROOMS DELETE-method:")
    response = requests.delete(f"{BASE}{room}{room_id}")  # (make sure to somehow verify it's the creator of the room calling this method)
    print(f"room nr {room_id} deleted: {response}")


def start_conversation(chatbot, user_id, room_id):  # /api/room/<int:room_id>/<int:user_id>/messages
    msg = chatbot.respond("start conversation")
    alias = chatbot.respond("alias")
    msg_json = {"user_id": user_id, "username": alias, "message": msg}
    response = requests.post(f"{BASE}{room}{room_id}/{user_id}/messages", msg_json)
    print("------------------------------------------------------------")
    print("starting conversation in chat-room - MESSAGES2 POST-method:")
    msg = response.json()
    return msg


def recieve_messages(user_id, room_id):  # /api/room/<int:room_id>/<int:user_id>/messages
    response = requests.get(f"{BASE}{room}{room_id}/{user_id}/messages")
    msg = response.json()
    for m in msg['messages']:
        if m is not None and m['user_id'] != user_id:
            format_and_print_msg(m)


def format_and_print_msg(msg):
    print(f"{msg['username']} says: {msg['message']} ")


def format_and_print_room(chatrooms):
    print("available rooms are: ")
    for r in chatrooms['rooms']:
        print(r['roomname'])


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
            #  msg = recieve_messages(user_id, room_id)

            # if msg['message'] == "bye":
            #     in_chatroom = leave_chatroom(user_id, room_id)
            delete_chatroom(room_id)
            in_chatroom = False

        connected = False


def client_connected_to_server2(chatbot):
    user_id = register_user(chatbot)
    connected = True
    while connected:
        available_rooms = get_all_chatrooms(user_id)
        room_id = choose_room(available_rooms)
        in_chatroom = join_chatroom(user_id, room_id)
      #  while in_chatroom:
        recieve_messages(user_id, room_id)
        connected = False

    print("bot disconnected")


bot = julia()  # starting chatbot
client_connected_to_server(bot)

bot2 = alex()
client_connected_to_server2(bot2)

# bot3 = huzeyfe()
# client_connected_to_server(bot3)
# må sende med user_id og room_id, maybe i client_connected_to_server(bot, room_id_user_id
