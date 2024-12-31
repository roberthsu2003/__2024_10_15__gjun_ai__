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
    response = model.generate_content(f"{question},回應請輸出成為html格式")
    html_format = response.text
    html_format = html_format.replace("```html","").replace("```","")
    return html_format

@app.route('/hello')
def hello():
    return 'Hello, World'