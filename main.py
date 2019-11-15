from flask import Flask, escape, request
from flask import json,jsonify
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def hello():
    return "OK"
if  __name__ == "__main__":
    app.run()