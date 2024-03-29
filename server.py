from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import socket

app = Flask(__name__)
api = Api(app)

# USER POST parser
users_post = reqparse.RequestParser()
users_post.add_argument('username', type=str, required=True, help="username is required")  # username
users_post.add_argument('user_id', type=int, required=False)

# up to us if it's going to be an array or database in final version (SQL-alchemy?)
users = {"user_register": []}
global user_counter  # temporary solution for user ID's when registering users
user_counter = 0


def user_not_exist_abort(user_id):  # abort if trying to use non-existing user_id
    for user in users['user_register']:
        if user['user_id'] == int(user_id):
            return
    abort(404, message="User not found")


def user_does_exist_abort(user_id):  # abort if overwriting existing user_id
    for user in users['user_register']:
        if user['user_id'] == user_id:
            abort(409, message="User already exists")


class User(Resource):  # /api/user/<int:user_id>

    def get(self, user_id):  # GET a used, by id
        user_not_exist_abort(user_id)
        for user in users['user_register']:
            if user['user_id'] == user_id:
                return user, 200

    def delete(self, user_id):
        user_not_exist_abort(user_id)
        for i, user in enumerate(users['user_register']):
            if user['user_id'] == user_id:
                users['user_register'].pop(i)
        return '', 204


class Users(Resource):

    def get(self):  # GET ALL users!
        args = request.get_json()
        user_not_exist_abort(args['user_id'])
        return users  # I don't see how this method can guarantee there's a registered user calling it.

    def post(self):  # register a user
        global user_counter
        user_id = user_counter
        user_counter += 1  # incrementing global variable each time user is registered
        args = users_post.parse_args()
        args['user_id'] = user_id
        users['user_register'].append(args)
        return user_id, 201  # returning the user ID


api.add_resource(User, "/api/user/<int:user_id>")  # adding User as a resource
api.add_resource(Users, "/api/users")  # adding Users as a resource

messages = {"messages": []}

message_post = reqparse.RequestParser()
message_post.add_argument('user_id', type=int, required=True, help='Enter your userid')
message_post.add_argument('username', type=str, required=True, help='Enter your username')
message_post.add_argument('message', type=str, required=True, help='Add a message...')
message_post.add_argument('room_id', type=int, required=True, help='You need a room id to get messages from')


class Message(Resource):

    def get(self, room_id):  # get last message
        args = request.get_json()
        user_id = args['user_id']
        user_not_exist_abort(user_id)
        room_abort_not_exist(room_id)
        all_messages_in_room = []
        if len(messages['messages']) == 0:
            return "", 404
        for message in messages['messages']:
            if message['room_id'] == room_id:
                all_messages_in_room.append(message)
        last_message = all_messages_in_room[len(all_messages_in_room) - 1]
        return last_message, 200


class Messages(Resource):

    def get(self, room_id, user_id):  # get all messages
        room_abort_not_exist(room_id)
        user_not_exist_abort(user_id)
        abort_if_not_member(room_id, user_id)
        message_list = []
        for m in messages['messages']:
            if m['room_id'] == room_id:
                message_list.append(m)
        if len(message_list) == 0:
            return "no messages", 404
        return message_list, 200

    def post(self, room_id, user_id):
        room_abort_not_exist(room_id)
        user_not_exist_abort(user_id)
        abort_if_not_member(room_id, user_id)
        args = message_post.parse_args()
        messages['messages'].append(args)
        return args, 200


api.add_resource(Message, "/api/room/<int:room_id>/messages")
api.add_resource(Messages, "/api/room/<int:room_id>/<int:user_id>/messages")

# ####################### ROOMS ################################

rooms = {"rooms": []}
global roomsCounter
roomsCounter = 0

rooms_post = reqparse.RequestParser()
rooms_post.add_argument('room_id', type=int, required=False)
rooms_post.add_argument('roomname', type=str, required=True, help='A name for your chat room')
rooms_post.add_argument('creator', type=int, required=True, help='The user id of the creator is required')
rooms_post.add_argument('password', type=str, help='Optional password if you dont want just anyone to join')


def room_abort_not_exist(room_id):
    if 0 <= room_id:
        for room in rooms['rooms']:
            if room.room_id == room_id:
                return
        return abort(404, message="Chatroom not found")
    return abort(410, messages="No existing rooms")


class Room(Resource):  # "/api/room/<int:room_id>"

    def get(self, room_id):
        args = request.get_json()
        user_id = args['user_id']
        user_not_exist_abort(user_id)
        room_abort_not_exist(room_id)
        for room in rooms['rooms']:
            if room.room_id == room_id:
                return room, 200

    def delete(self, room_id):  # check if creator is the only member in members before deleting
        args = request.get_json()
        user_id = args['user_id']
        user_not_exist_abort(user_id)
        room_abort_not_exist(room_id)
        for i, r in enumerate(rooms['rooms']):
            if r.room_id == room_id and r.creator == user_id:
                rooms['rooms'].pop(i)
                return '', 204


class Rooms(Resource):  # "/api/rooms, { json }

    def get(self):  # get all chatrooms
        args = request.get_json()
        user_not_exist_abort(args['user_id'])
        return rooms

    def post(self):  # create a new chatroom
        args = rooms_post.parse_args()
        if "creator" in args:
            user_not_exist_abort(args['creator'])
            global roomsCounter
            index = roomsCounter
            roomsCounter += 1
            args['room_id'] = index
            rooms['rooms'].append(args)
            return index, 201


api.add_resource(Room, "/api/room/<int:room_id>")
api.add_resource(Rooms, "/api/rooms")

members = {'members': []}
global member_count
member_count = 0


def member_abort_does_exist(user_id):  # abort if the user is already added to the room
    if user_id in members:
        abort(409, message="User already in the chat or another chat room")


def abort_if_not_member(room_id, user_id):
    for m in members['members']:
        if m['user_id'] == user_id and m['room_id'] == room_id:
            return
    return abort(404, message="You do not have access to the messages")


member_post = reqparse.RequestParser()
member_post.add_argument('room_id', type=int, required=True, help='Room ID is required')
member_post.add_argument('user_id', type=int, required=True, help='User ID is required')


# member_post.add_argument('alias', type=str, required=True, help='alias required')


class Members(Resource):  # /api/room/<room-id>/members
    def get(self, room_id):  # GET ALL members in the room
        args = request.get_json()
        user_id = args['user_id']
        user_not_exist_abort(user_id)
        room_abort_not_exist(room_id)
        abort_if_not_member(room_id, args['user_id'])
        room_members = []
        for m in members['members']:
            if m['room_id'] == room_id:
                room_members.append(m)
        return room_members, 200

    def post(self, room_id):  # ADD a user to the room
        args = member_post.parse_args()
        user_id = args.get('user_id')
        user_not_exist_abort(user_id)  # validerer
        room_abort_not_exist(room_id)
        member_abort_does_exist(user_id)
        global member_count  # lager member
        index = member_count
        member_count += 1
        members['members'].append(args)
        return index, 201

    def delete(self, room_id):
        args = request.get_json()
        user_id = args['user_id']
        user_not_exist_abort(user_id)
        room_abort_not_exist(room_id)
        abort_if_not_member(room_id, user_id)
        for i, m in enumerate(members['members']):
            if m.room_id == room_id:
                members['members'].pop(i)
                return '', 204


api.add_resource(Members, "/api/room/<int:room_id>/members")

# ########################## SOCKETS ################################
'''
socketRunning = True
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 2345
ip = "localhost"
serverSocket.bind((ip, port))
serverSocket.listen()
room_size = 1

while socketRunning:
    connectedClients = []
    users = []
    client, address = serverSocket.accept()
    connectedClients.append(client)
    for c in connectedClients:
        user_id = c.recv(2048).decode()
        users.append(user_id)
    
    for c in connectedClients:
        c.close()
    socketRunning = False
    '''

if __name__ == "__main__":
    app.run()  # change debug when when we're not testing anymore
