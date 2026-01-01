from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import AuthService
from app.api.deps import get_db, require_role

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(data: UserCreate, db: Session = Depends(get_db)):
    return AuthService.register(db, data.email, data.password)


@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    return AuthService.login(db, data.email, data.password)


@router.get("/admin")
def admin_dashboard(
    user = Depends(require_role("admin"))
):
    return {"message": "Acceso permitido"}
