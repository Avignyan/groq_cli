# Use Python 3.12 slim as the base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    BUILD_DATE="2025-06-12 14:04:28" \
    CREATED_BY="Avignyan"

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code (all Python files)
COPY *.py .
COPY .env .

# Set the entrypoint
ENTRYPOINT ["python", "main.py"]

# Default command (can be overridden)
CMD ["-i"]