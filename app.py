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
      consent_form = dictionary['consent_form']
      privacy_agreement = dictionary['privacy_agreement']
      emergency_contact_user_id_1 = dictionary['emergency_contact_user_id_1']
      emergency_contact_user_id_2 = dictionary['emergency_contact_user_id_2']
      query = 'INSERT INTO setmd.patients (user_id,consent_form,privacy_agreement,emergency_contact_user_id_1,emergency_contact_user_id_2) VALUES (%s,%s,%s,%s,%s)'
      vals = (uid,consent_form,privacy_agreement,emergency_contact_user_id_1,emergency_contact_user_id_2)
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

if __name__ == '__main__':
    app.run(host='0.0.0.0')