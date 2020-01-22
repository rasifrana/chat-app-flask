import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomkey123"
messages = []


def add_message(username, message):
    """Add messages to messages List"""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}
    messages.append(messages_dict)


@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with instruction"""

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")

# route for username
@app.route("/<username>")
def user(username):
    """Display Chat Message"""
    return "<h1>Welcome, {0} </h1> {1}".format(username, messages)

# route for user chat
@app.route("/<username>/<message>")
def send_message(username, message):
    """Create new message and redirect to chat page"""
    add_message(username, message)
    return redirect("/" + username)


app.run(host=os.getenv("IP"),
        port=os.getenv("PORT"),
        debug=True)
