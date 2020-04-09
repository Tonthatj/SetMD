# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:08:10 2020

@author: Jonathan
"""


from os import environ
from flask import Flask, jsonify, request
import json
from psycopg2 import connect, sql


try:
    
    
    
    conn = connect (
        dbname = 'setmd',
        user = "postgres",
        host = "setmd-db.ceij67ce3ano.us-east-2.rds.amazonaws.com",
        password = "Boss1234"
    )

    cur = conn.cursor()
except Exception as e:
    print("I am unable to connect to the database", e)

app = Flask(__name__, template_folder='templates')


@app.route('/create/user', methods=['POST'])
def create_user():    
  dictionary = dict(json.loads(request.data))
  
  name = dictionary["name"]
  email = dictionary["email"]
  phone = dictionary["phone"]
  role = dictionary["type"]
  disabled = dictionary["disabled"]
    
  sql = "INSERT INTO setmd.users (name, email, phone, type, disabled) VALUES (%s, %s, %s, %s, %s)"
  val = (name,email,phone,role,disabled)
  cur.execute(sql, val)

  query = ("SELECT id FROM setmd.users WHERE name = %s")
  
  uid = cur.execute(query, name)
  print(uid)
  
  
def create_user_test():    
  cur = conn.cursor()
  sql2 = "INSERT INTO setmd.users (name, email, phone, role, disabled) VALUES ('Jon Tonthat', 'jwtonthat@gmail.com', 9783176486, 'GOD', false)"
  cur.execute(sql2)

  query = ("SELECT id FROM setmd.users WHERE name = 'jon'")
  
  uid = cur.execute(query)
  print(uid)

  
if __name__ == '__main__':
    create_user_test()
    app.run(host='0.0.0.0', port=5001, debug=False, threaded=False)
    
