import pathlib
from flask import Flask
from reportMonaco import report


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'
