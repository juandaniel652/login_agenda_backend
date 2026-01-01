from fastapi import FastAPI
from app.api.v1.auth import router as auth_router

app = FastAPI(
    title="Auth Service",
    description="Authentication and authorization API",
    version="1.0.0",
)

# Routers
app.include_router(
    auth_router,
    prefix="/api/v1",
    tags=["Authentication"],
)

# Root endpoint
@app.get("/", tags=["System"])
def root():
    return {
        "service": "auth-service",
        "status": "running",
        "version": app.version,
    }

# Health check (usado por infra / monitoreo)
@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok"}
