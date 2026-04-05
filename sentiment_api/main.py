from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router as api_router

def get_application() -> FastAPI:
    """
    Create and configure the FastAPI application instance.
    This factory pattern is better for testing and MLOps scalability.
    """
    application = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="Modular FastAPI application for text sentiment analysis structured for MLOps",
    )

    # Include the API router with a prefix
    application.include_router(api_router, prefix=settings.API_V1_STR)

    @application.get("/")
    async def root():
        return {
            "message": f"Welcome to {settings.PROJECT_NAME}.",
            "docs_url": "/docs"
        }

    return application

app = get_application()
