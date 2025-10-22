# Provide a lightweight Python 3.9 environment based on Debian Buster.
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app


# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Create an output directory inside the container
RUN mkdir -p /app/output

# Command to run when the container starts
CMD ["python", "script.py"]