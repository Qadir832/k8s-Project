# Base image Python ka lightweight version
FROM python:3.9-slim

# Container ke andar working directory
WORKDIR /app

# Requirements file ko container mein copy karein
COPY requirements.txt .

# Dependencies install karein
RUN pip install --no-cache-dir -r requirements.txt

# Baqi saara backend ka code copy karein
COPY . .

# FastAPI default port 8000 par chalti hai
EXPOSE 8000

# App ko run karne ki command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]