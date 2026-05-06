from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps!"

@app.route("/secret")
def secret():
    return os.getenv("SECRET_KEY")

app.run(host="0.0.0.0", port=5000)
