# Provide a lightweight Python 3.9 environment based on Debian Buster.
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app


# Copy the requirements file and install dependencies
COPY requirements.txt script.py /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose port 80 for the web server
EXPOSE 80

# Command to run when the container starts
CMD ["python", "script.py"]