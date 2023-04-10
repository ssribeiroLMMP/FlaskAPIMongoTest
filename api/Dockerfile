# Use a Python 3.9 image as the base
FROM python:3.6

# Copy api folder into the container directory
ADD /api /api

# Set the working directory to /api
WORKDIR /api

# Use a Python 3.9 image as the base
RUN pip install -r requirements.txt

RUN adduser --disabled-password --gecos '' your_username && \
    echo "admin:admin" | chpasswd
