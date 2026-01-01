from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories.user_repository import UserRepository
from app.core.security import (
    verify_password,
    create_access_token,
    hash_password
)
from app.models.user import User


class AuthService:

    @staticmethod
    def register(db: Session, email: str, password: str):
        if UserRepository.get_by_email(db, email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya está registrado"
            )

        user = User(
            email=email,
            password_hash=hash_password(password)
        )

        UserRepository.create(db, user)
        return {"message": "Usuario creado correctamente"}

    @staticmethod
    def login(db: Session, email: str, password: str) -> dict:
        user = UserRepository.get_by_email(db, email)

        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas"
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Usuario deshabilitado"
            )

        token = create_access_token({
            "sub": str(user.id),
            "role": user.role
        })

        return {
            "access_token": token,
            "token_type": "bearer"
        }
