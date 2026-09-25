"""STOCKSENSE Backend Configuration.

Environment-configurable settings for API, authentication, database, and CORS.
"""

import os
from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent

def get_cors_origins() -> list[str]:
    env_origins = os.getenv("CORS_ORIGINS")
    if env_origins:
        return [o.strip() for o in env_origins.split(",") if o.strip()]
    return [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "*",
    ]

class Settings(BaseModel):
    PROJECT_NAME: str = "STOCKSENSE"
    PRODUCT_TITLE: str = "STOCKSENSE — AI-Powered Inventory Intelligence & Demand Forecasting Platform"
    TAGLINE: str = "Predict Demand. Prevent Stockouts. Make Smarter Inventory Decisions."
    VERSION: str = "2.0.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # Security & Auth
    SECRET_KEY: str = os.getenv(
        "STOCKSENSE_SECRET_KEY",
        os.getenv("SECRET_KEY", "stocksense-super-secret-production-key-2026")
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    
    # Server Binding
    HOST: str = os.getenv("HOST", "0.0.0.0" if os.getenv("ENVIRONMENT") == "production" else "127.0.0.1")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # Database
    DB_PATH: str = os.getenv(
        "SMARTSTOCK_DB_PATH",
        os.getenv("DATABASE_PATH", str(BASE_DIR / "data" / "smartstock.db"))
    )
    
    # CORS
    CORS_ORIGINS: list[str] = get_cors_origins()

settings = Settings()
