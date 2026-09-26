FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    nodejs \
    npm \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Devin CLI (placeholder - adjust based on actual install method)
RUN npm install -g @devin/cli || echo "Devin CLI install placeholder"

# Copy application files
COPY scripts/ /app/scripts/
COPY .devin/ /app/.devin/

# Create directories for outputs
RUN mkdir -p /app/scan-results /app/reports

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "scripts/run_security_scan.py"]
