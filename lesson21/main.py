from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/<string:name>")
def index(name:str=""):
    return f"<h1>Hello,{name}您好!</h1>"

@app.route('/hello')
def hello():
    return 'Hello, World'