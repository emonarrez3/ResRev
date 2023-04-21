from flask import Flask, render_template, redirect, Blueprint, url_for
from pymongo import MongoClient
from flask_cors import CORS

restaurants = Blueprint('restaurants', __name__)

CORS(restaurants)

client = MongoClient('mongodb+srv://sc_delaEmi:u2JsEd0nzYssgaMd@cluster0.8qczawe.mongodb.net/test', 5000)
db=client['test']
res = db.restaurants


@restaurants.route("/restaurants")
def restaurant_list():
    arr = list(res.find({}, {"_id":0, "location":1, "hours":1, "link":1}))
    return render_template("./locations.html", title="locations", arr=arr)

