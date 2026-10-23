from argon2 import PasswordHasher

pwd = PasswordHasher()

def hash(password):
    return pwd.hash(password)

def verify(password, hashed_password):
    return pwd.verify(hashed_password, password)