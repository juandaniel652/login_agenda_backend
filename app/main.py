from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.auth import router as auth_router

app = FastAPI(
    title="Auth Service",
    description="Authentication and authorization API",
    version="1.0.0",
)

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "https://loginagenda.netlify.app/",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Routers
# =========================
app.include_router(
    auth_router,
    prefix="/api/v1",
    tags=["Authentication"],
)

# =========================
# System endpoints
# =========================
@app.get("/", tags=["System"])
def root():
    return {
        "service": "auth-service",
        "status": "running",
        "version": app.version,
    }


@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok"}
