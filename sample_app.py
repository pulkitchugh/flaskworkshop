from flask import Flask
app = Flask(__name__)

@app.route('/')
def running():
    return 'Flask is running!'
