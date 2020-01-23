import os
import requests
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "randomkey123"
messages = []

a = requests.get("https://api.binance.com/api/v1/ticker/24hr").json()
# print(a)


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
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")

# route for username
@app.route("/chat/<username>", methods=["GET", "POST"])
def user(username):
    """Add and Display Chat Message"""

    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(session["username"])

    return render_template("chat.html", username=username, chat_messages=messages)


app.run(host=os.getenv("IP"),
        port=os.getenv("PORT"),
        debug=True)
