# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, Response


app = Flask(__name__)

USERS = {}

GET = 'GET'
POST = 'POST'
DELETE = 'DELETE'


@app.route('/user/<username>', methods=[GET, DELETE])
def access_users(username):
    if request.method == GET:
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)
    elif request.method == DELETE:
        if username in USERS:
            del USERS[username]
            return Response(status=200)
        return Response(status=404)


@app.route('/user', methods=[POST])
def register_user():
    if request.method == POST:
        user_data = request.get_json()
        USERS.update(user_data)
        field, value = user_data.items()[0]
        created = USERS.get(field)
        return jsonify(created)


if __name__ == '__main__':
    app.run()
