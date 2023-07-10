from passlib.context import CryptContext
from decouple import config

SCHEMA = config('CRYPTO_SCHEMA')

pwd_context = CryptContext(schemes=[SCHEMA], deprecated="auto")

def verify_password(plain_password, hashed_password) -> bool:
    """Verify the passwords"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password) -> str:
    """Get the hashed password"""
    return pwd_context.hash(password)