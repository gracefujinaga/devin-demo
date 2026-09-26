FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY scripts/ /app/scripts/
COPY .devin/ /app/.devin/
COPY .env.example /app/.env.example

# Create directories for outputs
RUN mkdir -p /app/scan-results /app/reports /app/logs /app/pr_tracking

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "scripts/run_simple_scan.py"]
