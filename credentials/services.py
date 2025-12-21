import base64
import os
import hashlib
import hmac


import secrets
PBKDF2_ITERATIONS=260000
def generate_salt():
    return os.urandom(32)


def hash_password(password,salt):
   
   dk = hashlib.pbkdf2_hmac(           
        'sha256',
        password.encode(),
        salt,
        PBKDF2_ITERATIONS)
   return base64.b64encode(dk).decode()

    
def verify_password(password,hash,salt):
    return hmac.compare_digest(hash,hash_password(password,salt))
def generate_2fa_token():
    return secrets.token.hex(32)
