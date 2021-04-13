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
        (r"roomname", ["olafiaklinikken", "snacks", "Hogwarts"]),
        (r"start conversation", ["Hi everyone, welcome to the chat", "Hey guys, nice to see you're all here"]),
        (r"topic", ["I actually need some new recipies. I've been cooking the same food for three weeks in a row.",
                    "Are any of you into sports?", "Have you guys watched any good movies during lockdown?"]),
        (
            r"(.*) Hi(.*)|(.*) Hey(.*)|(.*)Welcome(.*)|(.*)Hello(.*)",
            ["Hiii, it's great to be here, I need lunch tips!"]),
        (r"(.*)food(.*)", ["What do you want? I'm mostly into vegetarian food, though the latest dish I descovered is "
                           "the Persian khoresh with lamb called ghormeh sabsi!"]),
        (r"bye", ["bye"]),
        (r"(.*)sport(.*)", ["Generally I'm more into art than sport. I watched La liga in 2019 when I lived with a "
                            "couple of Spanish guys, which was awesome, but I guess I think it's more exciting to "
                            "watch when someone has a local connection to the teams.",
                            "Hmm, I used to play soccer, volleyball and badminton. All awesome sports but I honestly "
                            "never prioritize playing anymore, now it's just random the few times I get to play.",
                            "I'm into dancing, guess it's not a sport really but Chicago-footwork jams and battles"
                            "looks sporty to me, haha."]),
        (r"(.*)film(.*)|(.*)movie(.*)", ["I've been re-watching Matrix every break since first year of uni, the first "
                                         "one is simply great. It's therefore a freaking mystery how the other two "
                                         "got so incredibly bad??",
                                         "Have anyone watched Brave New World? The tv-series on HBO, based on Aldous "
                                         "Huxley sci-fi novel from 1932. I'm not sure if I should get HBO "
                                         "subscription or not"]),
        # make some damage
    ]
    chatbot = Chat(pairs, reflections)
    return chatbot


def alex():
    pairs = [
        (r"username", ["alex"]),
        (r"alias", ["alexxx", "ale", "alez"]),
        (r"roomname", ["datanett gc", "the gang", "cabbage"]),
        (r"start conversation", ["Hiii girliesss, hope everybody is having a good day, welcome to the chat",
                                 "Heyy errybody, i made this soooo lets talk",
                                 "Hello and welcome to the gc :) hope we'll have a nice convo"]),
        (r"(.*) Hi(.*)|(.*) Hey(.*)|(.*) Welcome(.*)|(.*) Hello(.*)", ["Helluuu, happy to be here",
                                                                       "Ouuu fun a new chatroom"]),
        (r"bye", ["bye"]),
        (r"topic", ["Sooo what kind of food do you guys like?", "Well, i guess we could talk about sports",
                    "Do you guys have any favorite films", "What kind of movies or series do you guys watch?"]),
        (r"(.*)food(.*)", ["I looooove spicy food hihi", "I could eat every day, oh wait, i already do hahah",
                           "I love to make food, i also like baking, but i dont like pastries so not a good combo"]),
        (r"(.*)sport(.*)|(.*)sports(.*)", ["Ehheh I dont really watch or play any sports anymore",
                                           "Sports? Nope not for me", "I play games, not sports"]),
        (r"(.*)movies(.*)|(.*)movie(.*)", ["I like horror movies, but there hasn't really been any good ones lately",
                                           "Lovee all of the studio ghibli movies, nostalgia u know",
                                           "I like 'eternal sunshine of the spotless mind' cuz it feels like a dream hehe"])
    ]
    alex_bot = Chat(pairs, reflections)
    return alex_bot


def huzeyfe():
    pairs = [
        (r"username", ["Huzeyfe"]),
        (r"alias", ["uzi", "huzi", "theuzi123", "phoenix", "BigBoy2k"]),
        (r"roomname", ["Time for Val!", "Gaming room", "diskusjons toalett"]),
        (r"start conversation", ["Welcome to the gaming universe guys:)",
                                 "Heyyy bros!, long time no see. How are you?",
                                 "Bro im really sad, some one wanna talk?"]),
        (r"(.*) Hi (.*)|(.*) Hey (.*)|(.*)Welcome(.*)|(.*)Hello(.*)", ["heluu folks", "Merhaba dudes;)"]),
        (r"bye", ["bye"]),
        (r"topic",
         ["Dude i really hungry, down to get some food?", "sport if the best thing in the world, you guys agree?",
          "Did someone see the new movie last week?! Wow it was amazing!"]),
        (r"(.*)food(.*)", ["Bro cant you see that I love food? Like look at me dude!",
                           "I can really eat everything, it's starting to get a big problem",
                           "I'm not a big fan of proper food, but I can eat snacks anytime",
                           "Food?! fuck now i'm just thinking about chicken tikka masala, chicken curry, chicken "
                           "tandori, chicken biryani aaaaarghh",
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
        (r"username", ["josh"]),
        (r"alias", ["josh1405", "josh"]),
        (r"roomname", ["josh_chatroom", "Movies"]),
        (r"start conversation", ["Hello, what's up?", "Hi guys!",
                                 "Hey wanna watch a movie?",
                                 "Yo! Let's get some food.",
                                 "Hey, I'm going outside to play some sports. Do you guys want to join?"]),
        ("r(.*) Hi (.*)", ["Hey sport", "Hi, Food?"]),
        (r"topic", ["Are you guys hungry? Let's go get some food!",
                    "Sports! Can we talk about something else haha.",
                    "I've seen a lot of good films.",
                    "Who wants to go and watch a movie? I'll bring some popcorn :)"]),
        (r"(.*)vegetarian food(.*)", ["Vegetarian food sounds nice. I haven't had that in a while."]),
        (r"(.*)spicy(.*)", ["I don't like spicy food, cause I have a very low tolerance on spicy things haha."]),
        (
        r"(.*)dancing(.*)", ["I'm not reaaly good at dancing haha. My friend make fun of me whenever I try to dance :P",
                             "I tried to do tiktok dances but it didn't workout haha. I looked like a stick trying to "
                             "dance. rip"]),
        (r"(.*)volleyball(.*)", ["I had that at P.E. in high school. It was fun. Although whenever I get to serve it "
                                 "lowkey "
                                 "hurts haha."]),
        (r"(.*)not sports(.*)", ["Me too. ", "Saaaaammmme"]),
        (r"(.*)documentaries(.*)", ["Ooooo I love watching documentaries. I saw one about sports last time."]),
        (r"(.*)Matrix(.*)", ["I think I've heard about that movie. But I have never really seen it before"]),
        (r"(.*)hbo(.*)", ["I don't have an hbo subscription, maybe I should get one"]),
        (r"(.*)baking(.*)", ["Same, I also like to bake.", "What did you bake last time?"]),
        (r"(.*)horror(.*)", ["I don't like horror movies. It's not my kind of movie to watch."]),
        (r"(.*)eternal sunshine(.*)", ["I haven't heard of that movie. Why does it feel like a dream? haha"]),
        (r"(.*)look at me(.*)", ["Ikr, I didn't want to say anything, but you said so...."]),
        (r"(.*)chicken(.*)", ["Why are you tempting me. I'm so hungry rn but there's no food here."]),
        (r"(.*)anorexia(.*)", ["Whaaat me too, Let's go to therapy together :)"]),
        (r"(.*)boring(.*)", ["I agree"]),
        (r"(.*)star wars(.*)", ["I saw star wars when I was little, kinda don't remember anything about it haha."]),
        (r"(.*)series(.*)", ["I like series too, What kind are you watching now?"]),
        (r"bye", ["bye"]),
        (r"(.*)movie(.*)", ["What kind of movies do you like?",
                            "One time I saw a movie about food.",
                            "Have you guys seen the Avengers? I think it is a decent movie.",
                            "Do you guys have Netflix? There ara a lot of movies there", ]),
        (r"(.*)sport(.*)", ["I'm not keen on playing sports.",
                            "Whaaaat sports, Not interested haha. How about movies?",
                            "Did you know I was in a basketball team when I was 13 years old?",
                            "My cousins love to watch sports"]),
        (r"(.*)food(.*)", ["I love making food.",
                           "My favorite food is pasta. And I also like making them",
                           "I love to bake different kinds of pastries",
                           "Have you tried the food at the restaurant at the seaside",
                           "I saw this nice movie about food."])
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


def register_user(username):  # /api/users
    register = {'username': username}
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
    print("------------------------------------------------------------")
    print("getting all chat rooms - ROOMS GET-method:")
    response = requests.get(f"{BASE}{rooms}", json={'user_id': user_id})
    all_chatrooms = response.json()
    return all_chatrooms


def join_chatroom(user_id, room_id):  # /api/room/<int:room_id>/users
    print("------------------------------------------------------------")
    print("joining the chat-room - MEMBERS POST-method:")
    response = requests.post(f"{BASE}{room}{room_id}/members", {'room_id': room_id, 'user_id': user_id})
    print(response.json())


def find_room_id_for_roomname(roomname, all_rooms):
    for index, r in enumerate(all_rooms['rooms']):
        if r['roomname'] == roomname:
            return index
    return -1


def delete_chatroom(user_id, room_id):  # /api/room/<int:room_id>
    print("------------------------------------------------------------")
    print("creator of chat-room closing it - ROOMS DELETE-method:")
    response = requests.delete(f"{BASE}{room}{room_id}", json={'user_id': user_id})
    print(f"room nr {room_id} deleted: {response}")


def start_conversation(chatbot, user_id, room_id, alias):  # /api/room/<int:room_id>/<int:user_id>/messages
    msg = chatbot.respond("start conversation")
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
    for msg in messages:
        global last_msg_index
        if msg is not None and msg['user_id'] != user_id and i > last_msg_index:
            format_and_print_msg(msg)  # printing new messages from other users if index is bigger than last time
        i = i + 1
    last_msg_index = i


def recieve_last_message(user_id, room_id):
    response = requests.get(
        f"{BASE}{room}{room_id}/messages", json={'user_id': user_id})  # , {"user_id" : user_id} [ check MSG GET-method on server]
    msg = response.json()
    return msg


def get_all_members_of_room(user_id, room_id):
    response = requests.get(f"{BASE}{room}{room_id}/members", json={'user_id': user_id})
    members = response.json()
    return members


def format_and_print_msg(msg):
    print(f"{msg['username']} says: {msg['message']} ")


def format_and_print_room(chatrooms):
    print("available rooms are: ")
    for r in chatrooms['rooms']:
        print(r['roomname'])


def leave_all_members_chatroom(user_id, room_id):  # /api/room/<int:room_id>/<int:user_id>
    print("------------------------------------------------------------")
    print("leaving the chat-room - MEMBERS DELETE-method:")
    response = requests.delete(f"{BASE}{room}{room_id}/members", json={"user_id": user_id})
    print(f"members in room: {room_id} deleted {response}")


# ############################ Input Validation #####################################

def user_defined_bot():  # create prompt and input validation for each post.
    pass


def choose_bot():

    chatbot = None
    while chatbot is None:
        print("Choose a chatbot ('julia', 'alex', 'huzeyfe', 'josh' or 'user')")
        botname = input(">")
        if botname.lower() == "julia":
            chatbot = julia()
        elif botname.lower() == "alex":
            chatbot = alex()
        elif botname.lower() == "huzeyfe":
            chatbot = huzeyfe()
        elif botname.lower() == "josh":
            chatbot = josh()
        elif botname.lower() == "user":
            chatbot = "user"
        else:
            print("Invalid bot name. Only defined bot names are valid.")

    return chatbot


def create_or_join_room(bot, user_id):
    # updating registered rooms and loops this question until the user has the choice to join a room
    creating = False
    while True:
        if bot != "user":
            while len(get_all_chatrooms(user_id)['rooms']) < 1 or creating:
                print("Would you like to create a room? (Yes/No)")
                response = input(">")
                if response.lower() == "yes" or response.lower() == "y":
                    room_ID = create_chatroom(bot, user_id)
                    join_chatroom(user_id, room_ID)
                    return room_ID, True
                else:
                    creating = False
        print("Would you like to join an existing chatroom? Type: (Yes/No)")
        response = input(">")
        if response.lower() == "yes" or response.lower() == "y":
            room_id = validation_roomname(user_id)
            print(f"room ID for choosen room: {room_id}")
            return room_id, False
        else:
            creating = True


def validation_roomname(user_id):
    room_id = -1
    all_rooms = get_all_chatrooms(user_id)
    while room_id == -1 or room_id is None:
        print("Which chatroom would you like to join? Type: <room name>")
        format_and_print_room(all_rooms)
        roomname = input(">")
        for r in all_rooms['rooms']:
            if r['roomname'] == roomname:
                room_id = r['room_id']
        if room_id == -1 or room_id is None:
            print("Invalid room name. Try again.")
    return room_id


# ############################ Creator of chatroom chat-Protocol #####################################

def creator_chat_protocol(in_chatroom, bot, user_id, room_id, alias):
    while in_chatroom:
        time.sleep(10)
        recieve_unread_messages(user_id, room_id)
        last_msg = recieve_last_message(user_id, room_id)
        if last_msg_index > 10:
            last_msg = {"user_id": user_id, "message": bot.respond("Bye")}
            send_message(bot, user_id, room_id, last_msg, alias)
            time.sleep(10)
            leave_all_members_chatroom(user_id, room_id)
            delete_chatroom(user_id, room_id)
            in_chatroom = False
        else:
            send_message(bot, user_id, room_id, last_msg, alias)
    # if "condition ... sendmessage(bye) :
    # in_chatroom = False
    return in_chatroom  # returning a in_chatroom = False when chat is finished


# ############################ Joiner of chatroom chat-Protocol #####################################

def joiner_chat_protocol(in_chatroom, bot, user_id, room_id, alias):
    while in_chatroom:
        time.sleep(10)
        recieve_unread_messages(user_id, room_id)
        last_msg = recieve_last_message(user_id, room_id)
        if last_msg['message'] == "bye":
            global last_msg_index
            last_msg_index = -1
            in_chatroom = False
        else:
            send_message(bot, user_id, room_id, last_msg, alias)
    return in_chatroom


# ############################ SOCKET #####################################

def run_client():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(('localhost', 2345))

    # ################## Identifiers #######################
    bot = choose_bot()  # choosing bot from user input
    if bot == "user":
        print("Type in your username:")
        username = input(">")
    else:
        username = bot.respond("username")

    user_id = register_user(username)  # registering new user and receive user ID

    bot_active = True
    while bot_active:
        room_id, creator = create_or_join_room(bot, user_id)  # choosing to join/create room from user input
        alias = None
        if bot != "user":
            alias = bot.respond("alias")

        in_chatroom = True
        if creator:  # returning creator = True if a new room was created
            while len(get_all_members_of_room(user_id, room_id)) < 2:
                time.sleep(5)
            start_conversation(bot, user_id, room_id, alias)
            in_chatroom = creator_chat_protocol(in_chatroom, bot, user_id, room_id, alias)
        elif not creator and bot != "user":  # creator = False if the bot joined an existing room
            join_chatroom(user_id, room_id)
            # recieve_unread_messages(user_id, room_id)  # if joining an ongoing chatt, get all messages in it
            in_chatroom = joiner_chat_protocol(in_chatroom, bot, user_id, room_id, alias)
        else:
            recieve_unread_messages(user_id, room_id)
            in_chatroom = False

        if not in_chatroom:
            print("Do you want to exit the program? type: (Yes/No)")
            reply = input(">")
            if reply.lower() == "yes":
                bot_active = False
    clientSocket.close()


run_client()

# if bot reply = None :
# write reply to start new topic (OK, but i want to talk about food)
# Somehow keep connection open so clients can receive other bots replies
