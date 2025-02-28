# Use Python base image
FROM python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libyaml-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, wheel (important for building packages)
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install "cython<3.0.0" && pip install --no-build-isolation pyyaml==5.4.1

# Install Cython separately **before** installing other dependencies
RUN pip install --no-cache-dir Cython

# Set working directory
WORKDIR /app

# Copy requirements file first 
COPY requirements.txt .

RUN pip install --no-cache-dir --no-deps -r requirements.txt


# Copy the rest of the app
COPY . .

# Expose FastAPI port
EXPOSE 8080

# Run FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
