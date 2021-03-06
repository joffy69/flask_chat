import os
from flask import Flask, redirect

app = Flask(__name__)
messages=[]

def add_messages(username, message):
    """add messages to the messages list"""
    messages.append("{}: {}".format(username, message))

def get_all_messages():
    """get all messages and separate with a br"""
    return "<br>".join(messages)

@app.route('/')
def index():
    """ main page with instructions """
    return 'To send a message use /USERNAME/MESSAGE'

@app.route('/<username>')
def user(username):
    """display chat message"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())

@app.route('/<username>/<message>')
def send_message(username, message):
    """create a new message and redirect back to chat page"""
    add_messages(username, message)
    return redirect("/" + username)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)