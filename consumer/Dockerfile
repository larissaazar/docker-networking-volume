# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Create a directory for persistent data
RUN mkdir -p /data

# Define volume mount point
VOLUME /data

# Run the application
CMD ["python", "app.py"]
