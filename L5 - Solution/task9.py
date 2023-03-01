import re

def is_valid_password(password):
    if len(password) < 8 or len(password) > 20:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if re.search(r'[^a-zA-Z0-9\s]', password):
        return False
    return True