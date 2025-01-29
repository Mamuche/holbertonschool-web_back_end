#!/usr/bin/env python3
""" function that expects one string argument name password
and returns a salted, hashed password, which is a byte string."""


import bcrypt


def hash_password(password: str) -> bytes:
    """ Hash a password """
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())
