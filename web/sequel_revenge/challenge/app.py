import sqlite3
from flask import Flask, jsonify, render_template, request
from helpers import create_db, fill, sort_clubs


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/sort", methods=['POST'])
def sort():
    order_by = request.form['order_by']
    print(order_by)
    print(f"SELECT * FROM clubs ORDER BY {order_by} DESC")
    result = sort_clubs(order_by)
    return jsonify(result)


create_db()
fill()