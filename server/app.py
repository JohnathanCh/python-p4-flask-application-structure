#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome To Flask</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

@app.route('/<int:num>/<string:stuff>')
def stuff(num, stuff):
    return f'<h1>{stuff} is asdlkjasdg {num}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)