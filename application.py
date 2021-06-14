
from functions import response
from db import db
import hashlib
from flask import Flask, request
app = Flask(__name__)



@app.route('/auth', methods=["POST", "GET"])
def auth():

	email = str.lower(request.args['email'].replace(' ', ''))
	if(email == ''):
		return response('false', 'Empty email')

	password = request.args['password'].replace(' ', '')
	if(password == ''):
		return response('false', 'Empty password')

	password = hashlib.sha1(password.encode())
	password = password.hexdigest()
	
	with db.cursor() as cursor:
		cursor.execute("SELECT * FROM users WHERE email = %s AND pass = %s", (email, password))
		user = cursor.fetchall()

	if(len(user) == 0):
		return response('false', 'User not found')
	else:
		return response('true', 
			{
				"hash": user[0]['hash'],
				"id_user": user[0]['id_user']
			})


@app.route('/register', methods=["POST", "GET"])
def register():

	email = str.lower(request.args['email'].replace(' ', ''))
	if(email == ''):
		return response('false', 'Empty email')

	password = request.args['password'].replace(' ', '')
	if(password == ''):
		return response('false', 'Empty password')

	password = hashlib.sha1(password.encode())
	password = password.hexdigest()


	hash_db = email + password #test@mail.ru1234

	hash_db = hashlib.sha1(hash_db.encode())
	hash_db = password.hexdigest()


	# SELECT INSERT UPDATE DELETE
	
	with db.cursor() as cursor:
		cursor.execute("SELECT * FROM users WHERE email = %s AND pass = %s", (email, password))
		user = cursor.fetchall()
		id_user = cursor.last_id_insert() #15648

	
	if(len(user) == 0):
		return response('false', 'User not found')
	else:
		return response('true', {"id_user": id_user, "hash":hash_db})