#!/usr/bin/python2

import uuid
import hashlib

def hash_password(password):
    # userid is used to generate a random number
    salt = uuid.uuid4().hex # salt is stored in hexadecimal value
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    # hexdigest is used as an algorithm for storing password
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = raw_input('please enter the password: ')
hashed_password = hash_password(new_pass)

print('the string to store in the db is: ' + hashed_password)

old_pass = raw_input('re-enter new password: ')

if check_password(hashed_password, old_pass):
    print('you entered the right password!')
else:
    print('you entered the wrong password!')
