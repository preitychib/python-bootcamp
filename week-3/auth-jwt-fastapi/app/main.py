from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import settings
from .api import auth as auth_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router, prefix="/api/auth", tags=["Authentication"])

@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.
    """
    return {
        "message": "Hello Coders, Head over to docs for more",
        "docs": "/docs",
        "redoc": "/redoc"
    }