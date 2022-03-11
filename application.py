from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello world! This is my first Flask example !!' 