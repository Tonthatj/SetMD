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
        user = "setmd",
        host = "setmd-db.ceij67ce3ano.us-east-2.rds.amazonaws.com",
        password = "P455w0rd"
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
  role = dictionary["role"]
  disabled = dictionary["disabled"]
  
  
  if role[-1] == 'y':
      role = role.replace("y","ie")
  role = role +'s'
    
  
  query = "INSERT INTO setmd.users (name, email, phone, type, disabled) VALUES (%s, %s, %s, %s, %s)"
  vals = (name,email,phone,role,disabled)
  cur.execute(query, vals)
  conn.commit()

  query = ("SELECT id FROM setmd.users WHERE name = %s")
  cur.execute(query, name)
  conn.commit()
  result = cur.fetchall()
  
  uid = result[0][0]
  role = result[0][1]
  print(uid)
  
  
  
  
  
def create_user_test():    
  cur = conn.cursor()
  
  '''
  query = "INSERT INTO setmd.users (name, email, phone, role, disabled) VALUES ('Jon Tonthat', 'jwtonthat@gmail.com', 9783176486, 'GOD', false)"
  cur.execute(query)
  conn.commit()
  '''
  
  query = ("SELECT id, role FROM setmd.users WHERE name = 'Jon Tonthat'")
  cur.execute(query)
  result = cur.fetchall()
  
  
  uid = result[0][0]
  role = result[0][1]
  print(uid)

  types_of_roles = ["doctors", "patients", "productioncompanies", "productioncoordinators", "users", "setmedics"]
  if role in types_of_roles:
      print("yay")

  
if __name__ == '__main__':
    #create_user_test()
    app.run(host='0.0.0.0', port=5001, debug=False, threaded=False)
    
