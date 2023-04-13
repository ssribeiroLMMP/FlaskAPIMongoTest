# Use a Python 3.9 image as the base
FROM python:3.9

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends --assume-yes \
      openssh-server \
      iputils-ping

# Copy the Python script into the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install any necessary dependencies
# RUN pip install -r requirements.txt

RUN useradd -rm -d /home/admin -s /bin/bash -p admin admin
RUN echo "admin:admin" | chpasswd

EXPOSE 22

# Run the Python script continuously
ENTRYPOINT [ "/app/entrypoint.sh" ]