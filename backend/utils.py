import bcrypt

def hash_password(password: str) -> str:
    """Hash a password for storing."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(stored_password: str, provided_password: str) -> bool:
    """Check if a password matches the stored hash."""
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))