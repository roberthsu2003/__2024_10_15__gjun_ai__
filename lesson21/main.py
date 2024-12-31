from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello,徐國堂您好!</h1>"

@app.route('/hello')
def hello():
    return 'Hello, World'