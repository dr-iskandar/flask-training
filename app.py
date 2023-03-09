from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/testing')
def hello_aq():
    return 'Hello, A!'