#!/usr/bin/env python3
""""""


import bcrypt


def hash_password(password: str) -> bytes:
    """ Hash a password """
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())
