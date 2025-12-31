from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api import auth
from app.core.lifespan import lifespan

def create_application(create_tables: bool = False) -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="PythonUpskill - Healthcare Appointment System API",
        version="1.0.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        lifespan=lambda _: lifespan(_, create_tables=create_tables)
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
    
    return app

app = create_application()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
