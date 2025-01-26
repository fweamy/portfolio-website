from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

# Creates a list of dictionaries for featured cards
featured = [
    {
       "title": "Game Projects",
       "image": "itch.jpg",
        "desc": "RPG and puzzle game projects I have worked on, with a blend of horror and lighthearted narrative!",
        "link": "https://fweamy.itch.io/"
    },
    {
       "title": "Art & Design",
       "image": "behance.png",
        "desc": "My graphic design and visual identity work for events and organizations.",
        "link": "https://www.behance.net/fweamy"
    },  
    ]

# Creates a list of dictionaries for work showcase cards
projects = [
    {
       "title": "The Night Embrace",
       "image": "tne.gif",
       "tools": "Unity, C#, Adobe Photoshop",
        "desc": "A topdown game made with Unity tilemap system that includes an inventory system, game items represented as objects of classes, and pixel snapping for grahics display.",
        "link": "/"
    },
    {
       "title": "Pomotivity App",
       "image": "pomotivity.png",
       "tools": "Python, SQL",
        "desc": "A CLI productivity app where users can create, read, update, delete tasks in a to-do list stored in a SQLite3 database and set a task to work on with a pomodoro timer.",
        "link": "/"
    },
    {
       "title": "Personal Website",
       "image": "mysite.png",
       "tools": "Python, HTML, CSS, Javascript, Jinja, Flask framework, Bootstrap framework",
        "desc": "The website you are viewing right now!",
        "link": "/"
    },
    {
       "title": "Sorting Algorithms",
       "image": "sorting.png",
       "tools": "C",
        "desc": "A collection of attempts to implement sorting algorithms in C.",
        "link": "/"
    },
    {
       "title": "Musical Ping Pong",
       "image": "pingpong.png",
       "tools": "Unity, C#",
        "desc": "A ping pong game except every time the ball collides with a surface, it plays a note of the Mii theme.",
        "link": "/"
    },
    
]

@app.route("/")
def index():
    return render_template("index.html", featured=featured, projects=projects)

