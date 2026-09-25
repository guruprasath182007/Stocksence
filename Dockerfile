# ============================================================
# STOCKSENSE — PRODUCTION CONTAINER (FastAPI + ML Engine)
# ============================================================

FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080 \
    ENVIRONMENT=production

WORKDIR /app

# Install system dependencies (build-essential needed for any C-extensions if required)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python production dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend application, database layer, model artifacts, and pre-seeded database
COPY backend/ ./backend/
COPY smartstock/ ./smartstock/
COPY models/ ./models/
COPY data/ ./data/
COPY LOGO.png ./LOGO.png
COPY LOGO_circle.png ./LOGO_circle.png

# Expose container port (Cloud Run passes dynamic $PORT at runtime, defaults to 8080)
EXPOSE 8080

# Healthcheck for container liveness
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:${PORT:-8080}/api/health || exit 1

# Start Uvicorn ASGI server with dynamic port binding
CMD exec uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8080}
