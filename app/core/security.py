from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
import os

# =========================
# CONFIGURACIÓN GENERAL
# =========================


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
SECRET_KEY = os.getenv("loginjwt5738473847_e$siej&%$")


if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY no configurada")

from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
import os


pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

# =========================
# PASSWORDS
# =========================

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

# =========================
# JWT
# =========================

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()

    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt
