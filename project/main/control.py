from encodings import utf_8
import bcrypt



def hash_password(password):
    salt = bcrypt.gensalt(rounds=15)
    hashed = bcrypt.hashpw(password.encode('utf_8'), salt)
    return hashed









