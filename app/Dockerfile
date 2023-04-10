# Use a Python 3.9 image as the base
FROM python:3.9

# Copy the Python script into the container
COPY /app /app

# Set the working directory to /app
WORKDIR /app

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Run the Python script continuously
CMD while true; do python script.py; sleep 60; done