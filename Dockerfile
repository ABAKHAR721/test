# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install the dependencies with retry and increased timeout
RUN for i in 1 2 3; do \
    pip install --no-cache-dir --timeout=120 -r requirements.txt && break || \
    echo "Retrying... ($i)" && sleep 5; \
done

# Copy the entire project to the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
