import base64
import os
import hashlib
import hmac
from datetime import datetime
import secrets
PBKDF2_ITERATIONS=260000
def generate_salt():
    return base64.b64encode(os.urandom(32)).decode()
def hash_password(password,salt):
    decodekey=hashlib.pbkdf2_hmac('sha256',password.encode(),base64.b64encode(salt),PBKDF2_ITERATIONS)
    return base64.urlsafe_b64encode(decodekey).decode()
def verify_password(password,hash,salt):
    return hmac.compare_digest(hash,hash_password(password,salt))
def generate_2fa_token():
    return secrets.token.hex(32)
