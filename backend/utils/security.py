import bcrypt

def hash_password(password: str) -> str:
    """
    Hash a plain password using bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

def verify_password(password: str, hashed: str) -> bool:
    """
    Verify a plain password against the hashed password.
    Returns True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
