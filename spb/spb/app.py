from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import re
from datetime import datetime
import mysql.connector
from mysql.connector import FieldType
import connect

app = Flask(__name__)

dbconn = None
connection = None

def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(user=connect.dbuser, \
    password=connect.dbpass, host=connect.dbhost, \
    database=connect.dbname, autocommit=True)
    dbconn = connection.cursor()
    return dbconn

@app.route("/")
def home():
    return redirect("/currentjobs")

@app.route("/currentjobs")
def currentjobs():
    connection = getCursor()
    connection.execute("SELECT job_id,customer,job_date FROM job where completed=0;")
    jobList = connection.fetchall()
    return render_template("currentjoblist.html", job_list = jobList)    

@app.route("/currentjobs")
def currentjobs():
    cursor = getCursor()
    query = """
    SELECT j.job_id, c.name, j.job_date
    FROM job j
    JOIN customer c ON j.customer = c.customer_id
    WHERE j.completed = 0;
    """
    cursor.execute(query)
    jobList = cursor.fetchall()
    return render_template("currentjoblist.html", job_list=jobList)

@app.route("/addcustomer", methods=["GET", "POST"])
def add_customer():
    if request.method == "POST":
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        cursor = getCursor()
        cursor.execute("INSERT INTO customer (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
        return redirect(url_for('customer_list'))
    return render_template("addcustomer.html")

@app.route("/searchcustomer", methods=["GET", "POST"])
def search_customer():
    if request.method == "POST":
        search_term = request.form['search_term']
        cursor = getCursor()
        query = "SELECT * FROM customer WHERE name LIKE %s"
        cursor.execute(query, ('%' + search_term + '%',))
        results = cursor.fetchall()
        return render_template("searchresults.html", results=results)
    return render_template("searchcustomer.html")