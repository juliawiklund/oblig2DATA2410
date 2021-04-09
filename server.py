from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import socket

app = Flask(__name__)
api = Api(app)

# USER POST parser
users_post = reqparse.RequestParser()
users_post.add_argument('username', type=str, required=True, help="username is required")  # username
users_post.add_argument('password', type=str, required=True, help="password is required")  # password

# USER GET parser
user_id_check = reqparse.RequestParser()
user_id_check.add_argument('user_id', type=int, required=True, help="user ID required")  # user ID

# up to us if it's going to be an array or database in final version (SQL-alchemy?)
users = {"user_register": []}
global user_counter  # temporary solution for user ID's when registering users
user_counter = 0


def user_not_exist_abort(user_id):  # abort if trying to use non-existing user_id
    if 0 <= user_id < len(users['user_register']):
        if users['user_register'][user_id] is None:
            abort(404, message="User not found")


def user_does_exist_abort(user_id):  # abort if overwriting existing user_id
    if 0 <= user_id < len(users['user_register']):
        if users['user_register'][user_id] is not None:
            abort(409, message="User already exists")


class User(Resource):  # user_id is already registered

    def get(self, user_id):  # GET a used, by id
        user_not_exist_abort(user_id)
        return users['user_register'][user_id], 200

    def delete(self, user_id):
        user_not_exist_abort(user_id)
        del users['user_register'][user_id]
        return '', 204


class Users(Resource):

    def get(self):  # GET ALL users!
        args = user_id_check.parse_args()
        user_not_exist_abort(args['user_id'])
        return users  # I don't see how this method can guarantee there's a registered user calling it.

    def post(self):  # register a user
        global user_counter
        user_id = user_counter
        user_counter += 1  # incrementing global variable each time user is registered
        args = users_post.parse_args()
        users['user_register'].append(args)
        return user_id, 201  # returning the user ID


api.add_resource(User, "/api/user/<int:user_id>")  # adding User as a resource
api.add_resource(Users, "/api/users")  # adding Users as a resource

messages = {"messages": []}

message_post = reqparse.RequestParser()
message_post.add_argument('user_id', type=int, required=True, help='Enter your userid')
message_post.add_argument('username', type=str, required=True, help='Enter your username')
message_post.add_argument('message', type=str, required=True, help='Add a message...')


class Message(Resource):

    def get(self, room_id):
        # Skal returnere alle meldinger fra rommet
        room_abort_not_exist(room_id)
        return "melding fra rommet", 200


class Message2(Resource):

    def get(self, room_id, user_id):
        room_abort_not_exist(room_id)
        user_not_exist_abort(user_id)
        #  abort_if_not_member(room_id, user_id)
        return messages, 200

    def post(self, room_id, user_id):
        room_abort_not_exist(room_id)
        user_not_exist_abort(user_id)
        # abort_if_not_member(room_id, user_id)
        args = message_post.parse_args()
        messages['messages'].append(args)
        return args, 200


api.add_resource(Message, "/api/room/<int:room_id>/messages")
api.add_resource(Message2, "/api/room/<int:room_id>/<int:user_id>/messages")

# ####################### ROOMS ################################

rooms = {"rooms": []}
global roomsCounter
roomsCounter = 0

rooms_post = reqparse.RequestParser()
rooms_post.add_argument('roomname', type=str, required=True, help='A name for your chat room')
rooms_post.add_argument('creator', type=int, required=True, help='The user id of the creator is required')
rooms_post.add_argument('password', type=str, help='Optional password if you dont want just anyone to join')


def room_abort_not_exist(room_id):
    if 0 <= room_id < len(rooms['rooms']):
        if rooms['rooms'][room_id] is None:
            return abort(404, message="Chatroom not found")


class Room(Resource):

    def get(self, room_id):
        room_abort_not_exist(room_id)
        return rooms[room_id], 200

    def delete(self, room_id):  # check if creator is the only member in members before deleting
        args = user_id_check.parse_args()
        user_not_exist_abort(args['user_id'])
        room_abort_not_exist(room_id)
        del rooms['rooms'][room_id]
        return "Room deleted", 204


class Rooms(Resource):  # "/api/rooms, { json }

    def get(self):  # get all chatrooms
        args = user_id_check.parse_args()
        user_not_exist_abort(args['user_id'])
        if len(rooms) == 0:
            room_abort_not_exist(-1)  # no existing rooms
        return rooms

    def post(self):  # create a new chatroom
        args = rooms_post.parse_args()
        if "creator" in args:
            user_not_exist_abort(args['creator'])
            global roomsCounter
            index = roomsCounter
            roomsCounter += 1
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
    if members['members']['room_id'] != room_id and members['members']['user_id'] != user_id:
        return abort(404, message="You do not have access to the messages")


member_post = reqparse.RequestParser()
member_post.add_argument('room_id', type=int, required=True, help='Room ID is required')
member_post.add_argument('user_id', type=int, required=True, help='User ID is required')


class Members(Resource):  # /api/room/<room-id>/members
    def get(self, room_id):  # GET ALL members in the room
        # if USER ID exist - use the parser
        room_abort_not_exist(room_id)
        return members

    def post(self, room_id):  # ADD a user to the room
        args = member_post.parse_args()
        user_id = args.get('user_id')
        # sjekker alt
        room_abort_not_exist(room_id)
        user_not_exist_abort(user_id)
        member_abort_does_exist(user_id)
        # lager member
        global member_count
        index = member_count
        member_count += 1
        members['members'].append(args)
        return index, 201


api.add_resource(Members, "/api/room/<int:room_id>/members")

# ########################## SOCKETS ################################

socketRunning = True
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 2345
ip = "localhost"
serverSocket.bind((ip, port))
serverSocket.listen(4)
room_size = 1

while socketRunning:
    connectedClients = []
    # for x in range(room_size)
    client, address = serverSocket.accept()
    connectedClients.append(client)

    received = client.recv(1024).decode()
    for x in connectedClients:
        x.send(received.encode())

    for client in connectedClients:
        client.close()
    socketRunning = False

# if __name__ == "__main__":
#     app.run(debug=True)  # change debug when when we're not testing anymore
