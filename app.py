from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/works")
def works():
    return render_template("works.html")
