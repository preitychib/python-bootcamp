from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import appointment, auth, doctor, health
from app.core.config import settings
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

    app.include_router(health.router)
    app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
    app.include_router(doctor.router, prefix=f"{settings.API_V1_STR}/doctors", tags=["doctors"])
    app.include_router(appointment.router, prefix=f"{settings.API_V1_STR}/appointments", tags=["appointments"])
    return app

app = create_application(create_tables=True)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, log_level="info", workers=1, access_log=True, use_colors=True)
