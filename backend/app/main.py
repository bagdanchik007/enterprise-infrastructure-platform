
from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Infrastructure Management Platform",
    description=(
        "A platform for managing, monitoring, "
        "and automating enterprise IT infrastructure."
    ),
    version="0.1.0",
)


@app.get("/", tags=["General"])
async def root() -> dict[str, str]:
    """Return basic information about the application."""
    return {
        "application": "Enterprise Infrastructure Management Platform",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health", tags=["Monitoring"])
async def health_check() -> dict[str, str]:
    """Check whether the API is responding."""
    return {
        "status": "healthy",
        "service": "backend-api",
    }
