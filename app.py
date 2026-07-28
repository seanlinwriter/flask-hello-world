from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World from Ching-Hsiang Lin in CSPB 3308!'
