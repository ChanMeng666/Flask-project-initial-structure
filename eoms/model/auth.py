from eoms.model.db import get_cursor
import bcrypt
from flask import session

# This module handles user authentication, i.e. login
# and any function in realation to password hashinng, i.e. register, change password

# Authenciate username ans passwor, attempt to log user in
# Return True if both username and password pass authentication
# Otherwise return False
def login_by_username(username, password):
    # Query username in db user table
    query = """SELECT * 
            FROM user 
            WHERE username = %(username)s;
            """
    connection = get_cursor()
    connection.execute(
        query, 
        {
            "username": username
        },
        )
    user = connection.fetchone()
    # If user exists and is active
    if user and user.get('is_active'):
        # Check if password matches
        user_bytes = password.encode('utf-8')
        user_password = user['password'].encode('utf-8')
        if bcrypt.checkpw(user_bytes, user_password):
            session['loggedin'] = True
            session["user_id"] = user["user_id"]
            session["username"] = user["username"]
            session["role"] = user["role"]
            return True
    else:
        return False

# Add a user to db, default role is member
def add_user(username, password, role='customer'):
    # converting password to array of bytes 
    bytes = password.encode('utf-8') 
    # generating the salt 
    salt = bcrypt.gensalt() 
    # Hashing the password 
    hash = bcrypt.hashpw(bytes, salt) 
    query = """INSERT INTO user (`username`, `password`, `role`) 
            VALUES  (%(username)s, %(password)s, %(role)s);
            """
    connection = get_cursor()
    connection.execute(
        query,
        {
            'username': username,
            'password': hash,
            'role': role
        }
    )
    # Check if insert is successful
    # Return new user_id if successful
    # Otherwise return False
    if connection.rowcount == 1:
        return connection.lastrowid
    else:
        return False