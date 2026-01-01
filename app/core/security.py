from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
import os

# =========================
# CONFIGURACIÓN GENERAL
# =========================

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY no configurada")

# =========================
# PASSWORD CONTEXT
# =========================

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

# =========================
# PASSWORD HELPERS
# =========================

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

# =========================
# JWT
# =========================

def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None
) -> str:
    to_encode = data.copy()

    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
