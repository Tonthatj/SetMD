# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:18:00 2020

@author: Jonathan
"""


from flask import Flask,request
from psycopg2 import connect

try:
  conn = connect(
    dbname = 'setmd',
    user = 'setmd',
    host = 'setmd-db.ceij67ce3ano.us-east-2.rds.amazonaws.com',
    password = 'P455w0rd'
  )
  cur = conn.cursor()
except Exception as e:
  print('I am unable to connect to the database',e)

app = Flask(__name__)

@app.route('/create/user',methods=['POST'])
def create_user():
  dictionary = request.form

  name = dictionary['name']
  email = dictionary['email']
  phone = dictionary['phone']
  role = dictionary['role']
  disabled = dictionary['disabled']

  role = role + 's'

  query = 'INSERT INTO setmd.users (name,email,phone,role,disabled) VALUES (%s,%s,%s,%s,%s) RETURNING id'
  vals = (name,email,phone,role,disabled)
  cur.execute(query,vals)
  conn.commit()
  uid = cur.fetchone()[0]

  roles = ['doctors','patients','productioncoordinators']
  if role in roles:
    if role == 'doctors':
      office_location = dictionary['office_location']
      query = 'INSERT INTO setmd.doctors (user_id,office_location,is_god) VALUES (%s,%s,%s)'
      vals = (uid,office_location,False)
      cur.execute(query,vals)
      conn.commit()
    elif role == 'patients':
      date_of_birth = dictionary['date_of_birth']
      emergency_contact_user_id_1 = dictionary['emergency_contact_user_id_1']
      emergency_contact_relation_1 = dictionary['emergency_contact_relation_1']
      emergency_contact_user_id_2 = dictionary['emergency_contact_user_id_2']
      emergency_contact_relation_2 = dictionary['emergency_contact_relation_2']
      home_address = dictionary['home_address']
      consent_form = dictionary['consent_form']
      privacy_agreement = dictionary['privacy_agreement']
      query = 'INSERT INTO setmd.patients (user_id,date_of_birth,emergency_contact_user_id_1,emergency_contact_relation_1,emergency_contact_user_id_2,emergency_contact_relation_2,consent_form,privacy_agreement) VALUES (%s,%s,%s,%s,%s)'
      vals = (uid,date_of_birth,emergency_contact_user_id_1,emergency_contact_relation_1,emergency_contact_user_id_2,emergency_contact_relation_2,consent_form,privacy_agreement)
      cur.execute(query,vals)
      conn.commit()
    elif role == 'productioncoordinators':
      expiration_date = dictionary['expiration_date']
      w9_form = dictionary['w9_form']
      office_location = dictionary['office_location']
      query = 'INSERT INTO setmd.productioncompanies (user_id,expiration_date,w9_form,office_location) VALUES (%s,%s,%s,%s) RETURNING id'
      vals = (uid,expiration_date,w9_form,office_location)
      cur.execute(query,vals)
      conn.commit()
      pcid = cur.fetchone()[0]
      query = 'INSERT INTO setmd.productioncoordinators (user_id,production_company_id) VALUES (%s,%s)'
      vals = (uid,pcid)
      cur.execute(query,vals)
      conn.commit()

  return name + ' was created with the role ' + role




@app.route('/update/user',methods=['POST'])
def create_user():
  dictionary = request.form

  name = dictionary['name']
  email = dictionary['email']
  phone = dictionary['phone']
  role = dictionary['role']
  disabled = dictionary['disabled']

  role = role + 's'

  query = ("SELECT id, role FROM setmd.users WHERE email = %s")
  vals = (email)
  cur.execute(query,vals)
  conn.commit()
  uid = cur.fetchone()[0]
  
  query = 'UPDATE setmd.users (name,email,phone,role,disabled) WHERE user_id = %s VALUES (%s,%s,%s,%s,%s)'
  vals = (uid, name,email,phone,role,disabled)
  cur.execute(query,vals)
  conn.commit()
  
  

  roles = ['doctors','patients','productioncoordinators']
  if role in roles:
    if role == 'doctors':
      office_location = dictionary['office_location']
      query = 'UPDATE setmd.doctors (office_location,is_god) WHERE user_id = %s VALUES (%s,%s)'
      vals = (uid,office_location,False)
      cur.execute(query,vals)
      conn.commit()
    elif role == 'patients':
      date_of_birth = dictionary['date_of_birth']
      emergency_contact_user_id_1 = dictionary['emergency_contact_user_id_1']
      emergency_contact_relation_1 = dictionary['emergency_contact_relation_1']
      emergency_contact_user_id_2 = dictionary['emergency_contact_user_id_2']
      emergency_contact_relation_2 = dictionary['emergency_contact_relation_2']
      home_address = dictionary['home_address']
      consent_form = dictionary['consent_form']
      privacy_agreement = dictionary['privacy_agreement']
      query = 'UPDATE setmd.patients (date_of_birth,emergency_contact_user_id_1,emergency_contact_relation_1,emergency_contact_user_id_2,emergency_contact_relation_2,consent_form,privacy_agreement) WHERE user_id = %s VALUES (%s,%s,%s,%s)'
      vals = (uid,date_of_birth,emergency_contact_user_id_1,emergency_contact_relation_1,emergency_contact_user_id_2,emergency_contact_relation_2,consent_form,privacy_agreement)
      cur.execute(query,vals)
      conn.commit()
    elif role == 'productioncoordinators':
      expiration_date = dictionary['expiration_date']
      w9_form = dictionary['w9_form']
      office_location = dictionary['office_location']
      query = 'UPDATE setmd.productioncompanies (expiration_date,w9_form,office_location) WHERE user_id = %s VALUES (%s,%s,%s)'
      vals = (uid,expiration_date,w9_form,office_location)
      cur.execute(query,vals)
      conn.commit()
      

  return name + ' was updated'




if __name__ == '__main__':
    app.run(host='0.0.0.0')
