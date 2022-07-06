FROM python:3.6
ADD . /api
WORKDIR /api
RUN pip install -r requirements.txt