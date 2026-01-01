from fastapi import FastAPI
from src.api.v1.auth import router as auth_router

app = FastAPI(title="Auth Service", version="1.0.0")

app.include_router(auth_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
