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
global usr_id   # temporary solution for user ID's when registering users
usr_id = 0


def not_exist_abort(user_id):  # abort if trying to use non-existing user_id
    if user_id not in users:
        abort(404, message="User not found")


def does_exist_abort(user_id):  # abort if overwriting existing user_id
    if user_id in users:
        abort(409, message="User already exists")


class User(Resource):                   # user_id is already registered

    def get(self, user_id):
        not_exist_abort(user_id)
        return users[user_id], 200

    def delete(self, user_id):
        not_exist_abort(user_id)
        del users[user_id]
        return '', 204


class Users(Resource):

    def get(self):                      # if not empty, get all users
        if len(users) == 0:
            not_exist_abort(-1)
        return users

    def post(self):                     # register a user
        global usr_id
        usr_id += 1                     # incrementing global variable each time user is registered
        args = users_post.parse_args()
        users[usr_id] = args
        return usr_id, 201              # returning the user ID


api.add_resource(User, "/api/user/<int:user_id>")  # adding User as a resource
api.add_resource(Users, "/api/users")              # adding Users as a resource

if __name__ == "__main__":
    app.run(debug=True)  # change debug when when we're not testing anymore
