# starter code taken from VS Code's Website to start a flask app
# https://code.visualstudio.com/docs/python/tutorial-flask

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
