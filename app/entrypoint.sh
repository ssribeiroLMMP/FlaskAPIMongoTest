#!/bin/bash

service ssh start
service ssh restart
service ssh restart

while [ true ]; do
    python script.py
done