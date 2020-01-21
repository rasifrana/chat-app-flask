import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []


def add_message(username, message):
    """Add messages to messages List"""
    messages.append("{}: {}".format(username, message))


def get_all_messages():
    """Get all msgs and seperate with br tag"""
    return "<br>".join(messages)


@app.route("/")
def index():
    """Main page with instruction"""
    return "To send a message use /USERNAME/MESSAGE"

# route for username
@app.route("/<username>")
def user(username):
    """Display Chat Message"""
    return "<h1>Welcome, {0} </h1> {1}".format(username, get_all_messages())

# route for user chat
@app.route("/<username>/<message>")
def send_message(username, message):
    """Create new message and redirect to chat page"""
    add_message(username, message)
    return redirect("/" + username)


app.run(host=os.getenv("IP"),
        port=os.getenv("PORT"),
        debug=True)
