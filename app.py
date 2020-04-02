from os import environ
from flask import abort, Flask, jsonify, make_response, request, send_from_directory, render_template
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="#$#$#$*&",
  database="setmd-db"
)

mycursor = mydb.cursor()

app = Flask(__name__, template_folder='templates')


@app.route('/predict', methods=['POST'])
def create_client():    
  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
  val = ("John", "Highway 21")
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
