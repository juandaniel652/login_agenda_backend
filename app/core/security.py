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

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)
