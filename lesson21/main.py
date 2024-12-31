from flask import Flask
import os
from dotenv import load_dotenv
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key=os.environ['Gemini_API_KEY'])
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
@app.route("/<string:question>")
def index(question:str=""):
    return f"{question}"

@app.route('/hello')
def hello():
    return 'Hello, World'