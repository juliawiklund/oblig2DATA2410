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
global usr_id  # temporary solution for user ID's when registering users
usr_id = 0


def not_exist_abort(user_id):  # abort if trying to use non-existing user_id
    if user_id not in users:
        abort(404, message="User not found")


def does_exist_abort(user_id):  # abort if overwriting existing user_id
    if user_id in users:
        abort(409, message="User already exists")


class User(Resource):  # user_id is already registered

    def get(self, user_id):
        not_exist_abort(user_id)
        return users[user_id], 200

    def delete(self, user_id):
        not_exist_abort(user_id)
        del users[user_id]
        return '', 204


class Users(Resource):

    def get(self):  # if not empty, get all users
        if len(users) == 0:
            not_exist_abort(-1)
        return users

    def post(self):  # register a user
        global usr_id
        usr_id += 1  # incrementing global variable each time user is registered
        args = users_post.parse_args()
        users[usr_id] = args
        return usr_id, 201  # returning the user ID


api.add_resource(User, "/api/user/<int:user_id>")  # adding User as a resource
api.add_resource(Users, "/api/users")  # adding Users as a resource


# only user in the room can get messages - get all
# Route:/api/room/<room-id>/messages
class message(Resource):

    def get(self):
        return


# Only users who have joined the room can get or addmessages.
# Only registered user-id's should be permitted as <user-id
# get all and add one
# Route:/api/room/<room-id>/<user-id>/messages
class message2(Resource):

    def get(self):
        return

    def put(self):
        return


# api.add_resource(message, "/api/room/<room-id>/messages")
# api.add_resource(Message2, "/api/room/<room-id>/<user-id>/messages")


# ####################### ROOMS ################################

rooms = {}
global roomsCounter
roomsCounter = 0

rooms_post = reqparse.RequestParser()
rooms_post.add_argument('roomname', type=str, required=True, help='A name for your chat room')
rooms_post.add_argument('password', type=str, help='Optional password if you dont want just anyone to join')


def room_abort_not_exist(room_id):
    if room_id not in rooms:
        return abort(404, message="Chatroom not found")


class Room(Resource):

    def get(self, room_id):
        room_abort_not_exist(room_id)
        return rooms[room_id], 200

    def delete(self, room_id):
        room_abort_not_exist(room_id)
        del rooms[room_id]
        return "Room deleted", 204


class Rooms(Resource):

    def get(self):  # get all chatrooms
        if len(rooms) == 0:
            room_abort_not_exist(-1)  # no existing rooms
        return rooms

    def post(self):  # create a new chatroom
        global roomsCounter
        roomsCounter += 1
        args = rooms_post.parse_args()
        rooms[roomsCounter] = args
        return roomsCounter, 201


api.add_resource(Room, "/api/room/<int:room_id>")
api.add_resource(Rooms, "/api/rooms")


def check_room(room_id):
    if room_id not in rooms:
        abort(404, message="Room not found")


members = {}
global member_count
member_count = 0


class Member(Resource):
    def get(self, room_id, user_id):
        check_room(room_id)
        not_exist_abort(user_id)
        return members[user_id], 200

    def delete(self, room_id, user_id):
        check_room(room_id)
        not_exist_abort(user_id)
        del members[user_id]
        return "member kicked out", 204

    def post(self, room_id, user_id):
        check_room(room_id)
        not_exist_abort(user_id)
        if user_id not in members:
            global member_count
            member_count += 1
            members[user_id] = {"room_id": room_id, "user_id": user_id}
            return "User added as member", 201
        else:
            return "User already in the chat or another chat room", 404
    # maybe ta med put?


class Members(Resource):
    def get(self, room_id):
        if len(members) == 0:
            not_exist_abort(-1)
        return members


api.add_resource(Members, "/api/room/<int:room_id>/members")
api.add_resource(Member, "/api/room/<int:room_id>/<int:user_id>")

if __name__ == "__main__":
    app.run(debug=True)  # change debug when when we're not testing anymore
