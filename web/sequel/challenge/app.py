import sqlite3
from flask import Flask, jsonify, render_template, request
from helpers import create_db, search_for_product, fill


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/search", methods=['POST'])
def search():
    search = request.form['search']
    print("SELECT * FROM clubs WHERE name LIKE '%"+search+"%'")
    result = search_for_product(search)
    return jsonify(result)


create_db()
fill()