from flask import Flask, Markup

app = Flask(__name__)

@app.route('/')

def index():

    return Markup('<div>Hello %s</div>') % '<em>Flask</em>'