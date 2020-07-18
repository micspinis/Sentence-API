"""
Registration of a user 0 tokens
Each user gets 10 tokens
Store a sentence on our database for 1 token
Retrieve his stored sentence on out database for 1 token
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
