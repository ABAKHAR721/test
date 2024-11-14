# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install the dependencies
RUN pip install -r requirements.txt  # <-- Added RUN here

# Copy the entire project to the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_ENV=production

# Command to run the application
CMD ["python", "app.py"]
