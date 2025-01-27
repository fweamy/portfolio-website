from flask import Flask, redirect, render_template, request, session
import json

with open('data/main.json', 'r') as file:
    data = json.load(file)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", featured=data["featured"], projects=data["projects"])

@app.route("/message", methods=['GET', 'POST'])
def get_message():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        
        with open('data/msg.json', 'r+') as file:
            user_msg = json.load(file)
            user_msg['messages'].append(request.form)
            file.seek(0)
            json.dump(user_msg, file, indent=4)
        
        return redirect("/contact")
