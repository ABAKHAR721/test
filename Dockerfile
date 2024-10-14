# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /appp
COPY . /app

# Install any necessary dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port the app runs on n
EXPOSE 5000

# Define environment variable
ENV FLASK_ENV=production

# Define the command to run the application
CMD ["python", "app.py"]
