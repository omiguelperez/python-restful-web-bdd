# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, Response


app = Flask(__name__)

USERS = {}

GET = 'GET'


@app.route('/user/<username>', methods=[GET])
def access_users(username):
    if request.method == GET:
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)


if __name__ == '__main__':
    app.run()
