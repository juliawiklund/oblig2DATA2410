from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

# user input parsers
users_post = reqparse.RequestParser()
users_post.add_argument('username', type=str, required=True, help="username is required")  # username
users_post.add_argument('password', type=str, required=True, help="password is required")  # password

# up to us if it's going to be an array or database in final version (SQL-alchemy?)
users = {}
global user_counter  # temporary solution for user ID's when registering users
user_counter = 0


def user_not_exist_abort(user_id):  # abort if trying to use non-existing user_id
    if user_id not in users:
        abort(404, message="User not found")


def user_does_exist_abort(user_id):  # abort if overwriting existing user_id
    if user_id in users:
        abort(409, message="User already exists")


class User(Resource):  # user_id is already registered

    def get(self, user_id):
        user_not_exist_abort(user_id)
        return users[user_id], 200

    def delete(self, user_id):
        user_not_exist_abort(user_id)
        del users[user_id]
        return '', 204


class Users(Resource):

    def get(self):  # if not empty, get all users!
        if len(users) == 0:
            user_not_exist_abort(-1)
        return users  # I don't see how this method can guarantee there's a registered user calling it.

    def post(self):  # register a user
        global user_counter
        user_counter += 1  # incrementing global variable each time user is registered
        args = users_post.parse_args()
        users[user_counter] = args
        return user_counter, 201  # returning the user ID


api.add_resource(User, "/api/user/<int:user_id>")  # adding User as a resource
api.add_resource(Users, "/api/users")  # adding Users as a resource

messages = {}

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

        if members[user_id]['room_id'] == room_id and members[user_id]['user_id'] == user_id:
            return messages, 200

        # for m in members:
        #    if m.user_id == user_id:

        return abort(404, message="You do not have access to the messages")

    def post(self, room_id, user_id):
        # sjekk om det er en bruker i et room som poster
        room_abort_not_exist(room_id)
        args = message_post.parse_args()
        messages[user_id] = args
        return messages[user_id], 200


api.add_resource(Message, "/api/room/<int:room_id>/messages")
api.add_resource(Message2, "/api/room/<int:room_id>/<int:user_id>/messages")

# ####################### ROOMS ################################

rooms = {}
global roomsCounter
roomsCounter = 0

rooms_post = reqparse.RequestParser()
rooms_post.add_argument('roomname', type=str, required=True, help='A name for your chat room')
rooms_post.add_argument('creator', type=int, required=True, help='The user id of the creator is required')
rooms_post.add_argument('password', type=str, help='Optional password if you dont want just anyone to join')


def room_abort_not_exist(room_id):
    if room_id not in rooms:
        return abort(404, message="Chatroom not found")


class Room(Resource):

    def get(self, room_id):
        room_abort_not_exist(room_id)
        return rooms[room_id], 200

    def delete(self, room_id):  # check if creator is the only member in members before deleting
        room_abort_not_exist(room_id)
        del rooms[room_id]
        return "Room deleted", 204


class Rooms(Resource):  # "/api/rooms"

    def get(self):  # get all chatrooms
        if len(rooms) == 0:
            room_abort_not_exist(-1)  # no existing rooms
        return rooms

    def post(self):  # create a new chatroom
        args = rooms_post.parse_args()
        if "creator" in args:
            user_not_exist_abort(args['creator'])
            global roomsCounter
            roomsCounter += 1
            rooms[roomsCounter] = args
            return roomsCounter, 201


api.add_resource(Room, "/api/room/<int:room_id>")
api.add_resource(Rooms, "/api/rooms")

members = {}
global member_count
member_count = 0


def member_abort_does_exist(user_id):  # abort if the user is already added to the room
    if user_id in members:
        abort(409, message="User already in the chat or another chat room")


member_post = reqparse.RequestParser()
member_post.add_argument('room_id', type=int, required=True, help='Room ID is required')
member_post.add_argument('user_id', type=int, required=True, help='User ID is required')


# DENNE KAN FJERNES

class Member(Resource):  # /api/room/<room-id>/<user-id>
    def get(self, room_id, user_id):
        room_abort_not_exist(room_id)
        user_not_exist_abort(user_id)
        for number, m in enumerate(members):
            if m[number]['user_id'] == user_id:
                return m[number]['user_id'], 200
        return "Member not found", 404

    def delete(self, room_id, user_id):
        room_abort_not_exist(room_id)
        user_not_exist_abort(user_id)
        del members[user_id]
        return "member kicked out", 204


class Members(Resource):
    def get(self, room_id):
        room_abort_not_exist(room_id)
        if len(members) == 0:
            user_not_exist_abort(-1)
        return members

    def post(self, room_id):
        args = member_post.parse_args()
        user_id = args.get('user_id')
        # sjekker alt
        room_abort_not_exist(room_id)
        user_not_exist_abort(user_id)
        member_abort_does_exist(user_id)
        # lager member
        global member_count
        member_count += 1
        members[member_count] = args
        return member_count, 201


api.add_resource(Members, "/api/room/<int:room_id>/members")
# api.add_resource(Member, "/api/room/<int:room_id>/<int:user_id>")

if __name__ == "__main__":
    app.run(debug=True)  # change debug when when we're not testing anymore
