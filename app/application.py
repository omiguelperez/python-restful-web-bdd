# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, Response


app = Flask(__name__)

USERS = {}

GET = 'GET'
POST = 'POST'
DELETE = 'DELETE'
PUT = 'PUT'


@app.route('/user/list', methods=[GET])
def list_users():
    if request.method == GET:
        user_list = {}
        for key, value in USERS.items():
            user_list.update({'username': key, 'name': value.get('name')})
        return jsonify(user_list)


@app.route('/user/<username>', methods=[GET, DELETE, PUT])
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
    elif request.method == PUT:
        update_data = request.get_json()
        username, new_details = update_data.items()[0]
        if username in USERS:
            USERS.update(update_data)
            updated = USERS.get(username)
            return jsonify(updated)
        return Response(status=404)


@app.route('/user', methods=[POST])
def register_user():
    if request.method == POST:
        user_data = request.get_json()
        USERS.update(user_data)
        username, details = user_data.items()[0]
        created = USERS.get(username)
        return jsonify(created)


if __name__ == '__main__':
    app.run()
