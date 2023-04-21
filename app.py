from flask import Flask, jsonify, render_template, request, redirect, Blueprint
from flask_cors import CORS

#blueprints
from restaurants import restaurants

app = Flask(__name__)
app.register_blueprint(restaurants)

CORS(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("./home.html")