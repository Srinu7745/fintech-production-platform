from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="Fintech Transaction API")

@app.get("/")
def home():
    return {"message": "Fintech API is running"}

@app.get("/health/live")
def liveness():
    return {
        "status": "alive",
        "timestamp": datetime.now(timezone.utc)
    }

@app.get("/health/ready")
def readiness():
    # Later, this endpoint will check dependencies such as the database.
    database_available = True

    if not database_available:
        return {"status": "not_ready", "database": "unavailable"}

    return {"status": "ready", "database": "available"}