# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y procps

# Copy project code
COPY smart_devops_bot/ ./smart_devops_bot/

# Expose port for FastAPI
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "smart_devops_bot.web.server:app", "--host", "0.0.0.0", "--port", "8000"]