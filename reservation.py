from flask import Flask, render_template, redirect, Blueprint, url_for, request
from pymongo import MongoClient
from flask_cors import CORS

reservation = Blueprint('reservation', __name__)

CORS(reservation)

client = MongoClient('mongodb+srv://sc_delaEmi:u2JsEd0nzYssgaMd@cluster0.8qczawe.mongodb.net/test', 5000)
db=client['test']

@reservation.route('/reservation_page', methods=['POST'])
def respage():
    print(request.form["mydata"])
    return render_template("./reservation.html")