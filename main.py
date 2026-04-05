from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
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

    @application.get("/", response_class=HTMLResponse)
    async def root():
        html_path = os.path.join(os.path.dirname(__file__), "app", "frontend", "index.html")
        if os.path.exists(html_path):
            with open(html_path, "r", encoding="utf-8") as f:
                return HTMLResponse(content=f.read())
        return "Frontend not found"

    return application

app = get_application()
