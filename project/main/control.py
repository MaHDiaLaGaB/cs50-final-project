import bcrypt


def hash_password(password):
    salt = bcrypt.gensalt(rounds=15)
    password = password.encode('utf_8')
    hashed = bcrypt.hashpw(password, salt)
    return hashed
