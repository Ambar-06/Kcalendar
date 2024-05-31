# Base image
FROM python:3.10-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a non-root user
RUN useradd -m appuser

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip

# Set work directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Build stage for production
FROM base AS production

# Install Gunicorn
RUN pip install gunicorn

# Switch to non-root user
USER appuser

# Expose the port
EXPOSE 8000

# Run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kcalendar.wsgi:application"]
