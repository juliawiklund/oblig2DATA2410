from nltk.chat.util import Chat, reflections
import requests
import random
import socket
import time


# ################################# BOTS ###################################

def julia():
    pairs = [
        (r"username", ["julia"]),
        (r"alias", ["jullz", "wiklund", "j****w"]),
        (r"password", ["julia123", "wiklund456"]),
        (r"roomname", ["olafiaklinikken", "snacks", "Hogwarts"]),
        (r"start conversation", ["Hi everyone, welcome to the chat", "Hey guys, nice to see you're all here"]),
        (r"topic", ["food", "sport", "film", "movies"]),
        (r"(.*)Hi(.*)|(.*)Hey(.*)|(.*)Welcome(.*)|(.*)Hello(.*)", ["Hiii, it's great to be here, I need lunch tips!"]),
        (r"(.*)food(.*)", ["What do you want? I'm mostly into vegetarian food, though the latest dish I descovered is "
                           "the Persian khoresh with lamb called ghormeh sabsi!"]),
        (r"bye", ["bye"]),
        (r"(.*)ketchup(.*)", ["AAAH, elsker mackern", "Jeg liker friiies med ketchup"]),
        (r"(.*)sport(.*)", ["Generally I'm more into art than sport. I watched La liga in 2019 when I lived with a "
                            "couple of Spanish guys, which was awesome, but I guess I think it's more exciting to "
                            "watch when someone has a local connection to the teams.",
                            "Hmm, I used to play soccer, volleyball and badminton. All awesome sports but I honestly "
                            "never prioritize playing anymore, now it's just random the few times I get to play.",
                            "I'm into dancing, guess it's not a sport really but Chicago-footwork jams and battles"
                            "looks sporty to me, haha."]),
        (r"(.*)film(.*)|(.*)movie(.*)", ["I've been re-watching Matrix every break since first year of uni, the first "
                                         "one is simply "
                                         " great. It's therefore a freaking mystery how the other two got so incredibly bad??",
                                         "Have anyone watched Brave New World? The tv-series on HBO, based on Alons Huxley "]),
    ]
    chatbot = Chat(pairs, reflections)
    return chatbot


def alex():
    pairs = [
        (r"username", ["alex"]),
        (r"alias", ["alexxx", "ale", "alez"]),
        (r"password", ["ale123", "hvordanlagermanpassord123"]),
        (r"roomname", ["datanett gc", "the gang", "cabbage"]),
        (r"start conversation", ["Hiii girliesss, hope everybody is having a good day, welcome to the chat",
                                 "Wuddup errybody, i made this soooo lets talk",
                                 "Hello and welcome to the gc :) hope we'll have a nice convo"]),
        (r"(.*)Hi(.*)|(.*)Hey(.*)|(.*)Welcome(.*)|(.*)Hello(.*)", ["Helluuu, happy to be here",
                                                                   "Ouuu fun a new chatroom"]),
        (r"bye", ["byebyeee", "ttyl bye", "tnx for today:) byeee"]),
        (r"topic", ["Sooo what do you think about food guys?", "Well, i guess we can talk about sport",
                    "Do you have a favorie film?", "Lets talk about movies, what do you guys like?"]),
        (r"(.*)food(.*)", ["I looooove spicy food hihi", "I could eat every day, oh wait, i already do hahah",
                           "I love to make food, i also like baking, but i dont like pastries so not a good combo"]),
        (r"(.*)sport(.*)|(.*)sports(.*)", ["Ehheh I dont really watch or play any sports anymore",
                                           "Sports? Nope not for me", "I play games, not sports"]),
        (r"(.*)movies(.*)|(.*)movie(.*)|(.*)film(.*)",
         ["I like horror movies, but there hasn't really been any good ones lately",
          "Lovee all of the studio ghibli movies, nostalgia u know",
          "I like 'Sunshine in a spotless mind' cuz it feels like a dream hehe"]),
        (r"(.*)", ["I dont know how to respond to that"])
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
        (r"topic", ["food", "sport", "film", "movies"]),
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
    pairs = [
        (r"username", "josh"),
        (r"alias", ["josh1405", "josh"]),
        (r"password", "josh123"),
        (r"roomname", ["josh_chatroom", "Movies"]),
        (r"start conversation", ["Hello, what's up?", "Hi guys!"]),
        (r"topic", ["food", "sport", "film", "movies"]),
        (r"bye", ["See you!", "Bye"]),
        (r"(.*)movie(.*)", ["What kind of movies do you like?", "One time I saw a movie about food."]),
    ]
    chatbot = Chat(pairs, reflections)
    return chatbot


# ################################### Routes ####################################

BASE = "http://127.0.0.1:5000"
user = "/api/user/"
users = "/api/users"
rooms = "/api/rooms"
room = "/api/room/"

# ################################### Global Message variable ####################################
global last_msg_index
last_msg_index = -1


# ################################### Client Methods ####################################


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
    #  format_and_print_room(all_chatrooms)
    return all_chatrooms


# A method to choose randomly out of the given room indexes (If we'll implement bots choosing rooms automatically).
def choose_room(room_list):
    last_index = len(room_list['rooms']) - 1
    room_index = random.randint(0, last_index)
    return room_index


def join_chatroom(user_id, room_id):  # /api/room/<int:room_id>/users
    print("------------------------------------------------------------")
    print("joining the chat-room - MEMBERS POST-method:")
    response = requests.post(f"{BASE}{room}{room_id}/members", {'room_id': room_id, 'user_id': user_id})
    print(response.json())


def find_room_id_for_roomname(roomname, all_rooms):
    #  all_rooms = get_all_chatrooms(user_id)
    for index, r in enumerate(all_rooms['rooms']):
        if r['roomname'] == roomname:
            return index
    return -1


def delete_chatroom(room_id):  # /api/room/<int:room_id>
    print("------------------------------------------------------------")
    print("creator of chat-room closing it - ROOMS DELETE-method:")
    response = requests.delete(
        f"{BASE}{room}{room_id}")  # (make sure to somehow verify it's the creator of the room calling this method)
    print(f"room nr {room_id} deleted: {response}")


def start_conversation(chatbot, user_id, room_id, alias):  # /api/room/<int:room_id>/<int:user_id>/messages
    msg = chatbot.respond("start conversation")
    # alias = chatbot.respond("alias")
    msg_json = {"user_id": user_id, "username": alias, "message": msg, "room_id": room_id}
    response = requests.post(f"{BASE}{room}{room_id}/{user_id}/messages", msg_json)
    msg = response.json()
    print("------------------------------------------------------------")
    print("starting conversation in chat-room - MESSAGES2 POST-method:")
    format_and_print_msg(msg)


def send_message(bot, user_id, room_id, last_message, alias):
    if last_message is not None:
        bot_msg = bot.respond(last_message['message'])
        if bot_msg is None:
            bot_msg = bot.respond("topic")
        msg_json = {"user_id": user_id, "username": alias, "message": bot_msg, "room_id": room_id}
        response = requests.post(f"{BASE}{room}{room_id}/{user_id}/messages", msg_json)
        print("------------------------------------------------------------")
        format_and_print_msg(msg_json)
        msg = response.json()
        return msg


def recieve_unread_messages(user_id, room_id):  # /api/room/<int:room_id>/<int:user_id>/messages
    response = requests.get(f"{BASE}{room}{room_id}/{user_id}/messages")
    messages = response.json()
    i = 0
    for i, msg in enumerate(messages['messages']):
        global last_msg_index
        if msg is not None and msg['user_id'] != user_id and i > last_msg_index:
            format_and_print_msg(msg)  # printing new messages from other users if index is bigger than last time
    last_msg_index = i


def recieve_last_message(user_id, room_id):
    response = requests.get(
        f"{BASE}{room}{room_id}/messages")  # , {"user_id" : user_id} [ check MSG GET-method on server]
    msg = response.json()
    return msg


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


# ############################ Input Validation #####################################

def user_defined_bot():  # create prompt and input validation for each post.
    pass


def choose_bot():
    print("Choose a chatbot ('julia', 'alex', 'huzeyfe', 'josh' or 'user')")
    botname = input(">")
    chatbot = None
    if botname == "julia":
        chatbot = julia()
    elif botname == "alex":
        chatbot = alex()
    elif botname == "huzeyfe":
        chatbot = huzeyfe()
    elif botname == "josh":
        chatbot = josh()
    elif botname == "user":
        chatbot = user_defined_bot()
    else:
        print("you have to choose one of the options we defined")

    return chatbot


def create_or_join_room(bot, user_id):
    # check if there are any available rooms to actually join before offering it.
    print("Would you like to create or join an existing chatroom? Type: (create/join)")
    response = input(">")
    if response == "create":
        room_ID = create_chatroom(bot, user_id)
        return room_ID, True
    elif response == "join":
        room_id = validation_roomname(user_id)
        print(f"room ID for choosen room: {room_id}")
        return room_id, False
    else:
        print("Invalid answer, please try again")
        create_or_join_room(bot, user_id)


def validation_roomname(user_id):
    room_id = -1
    all_rooms = get_all_chatrooms(user_id)
    while room_id == -1 or room_id is None:
        print("Which chatroom would you like to join? Type: <room name>")
        format_and_print_room(all_rooms)
        roomname = input(">")
        room_id = find_room_id_for_roomname(roomname, all_rooms)
        if room_id == -1 or room_id is None:
            print("Invalid room name. Try again.")
    return room_id


# ############################ Creator of chatroom chat-Protocol #####################################

def creator_chat_protocol(in_chatroom, bot, user_id, room_id, alias):
    while in_chatroom:
        time.sleep(15)
        recieve_unread_messages(user_id, room_id)
        last_msg = recieve_last_message(user_id, room_id)
        send_message(bot, user_id, room_id, last_msg, alias)
    # if "condition ... sendmessage(bye) :
    # in_chatroom = False
    return in_chatroom  # returning a in_chatroom = False when chat is finished


# ############################ Joiner of chatroom chat-Protocol #####################################

def joiner_chat_protocol(in_chatroom, bot, user_id, room_id, alias):
    while in_chatroom:
        recieve_unread_messages(user_id, room_id)
        last_msg = recieve_last_message(user_id, room_id)
        if last_msg['message'] == "bye":
            leave_chatroom(user_id, room_id)
            in_chatroom = False
        else:
            send_message(bot, user_id, room_id, last_msg, alias)
            time.sleep(15)
    return in_chatroom


# ############################ SOCKET #####################################

def run_client():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(('localhost', 2345))

    # ################## Identifiers #######################
    bot = choose_bot()  # choosing bot from user input
    user_id = register_user(bot)  # registering new user and receive user ID
    room_id, creator = create_or_join_room(bot, user_id)  # choosing to join/create room from user input
    alias = bot.respond("alias")
    # ######################################################

    in_chatroom = True
    if creator:  # returning creator = True if a new room was created
        start_conversation(bot, user_id, room_id, alias)
        in_chatroom = creator_chat_protocol(in_chatroom, bot, user_id, room_id, alias)
    if not creator:  # creator = False if the bot joined an existing room
        join_chatroom(user_id, room_id)
        # recieve_unread_messages(user_id, room_id)  # if joining an ongoing chatt, get all messages in it
        in_chatroom = joiner_chat_protocol(in_chatroom, bot, user_id, room_id, alias)
    if not in_chatroom:
        clientSocket.close()


run_client()

# if bot reply = None :
# write reply to start new topic (OK, but i want to talk about food)
# Somehow keep connection open so clients can receive other bots replies
