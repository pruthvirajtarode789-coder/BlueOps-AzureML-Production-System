# Use an official Python runtime as a parent image
FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY api /app/api
COPY models /app/models
COPY deploy /app/deploy
COPY app /app/app

ENV PYTHONUNBUFFERED=1

# Uvicorn serving API
EXPOSE 8000

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
