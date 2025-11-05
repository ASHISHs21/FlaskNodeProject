# Use official Python base image
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the backend code
COPY . .

# Expose backend port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
