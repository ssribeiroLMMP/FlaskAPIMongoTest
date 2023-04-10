import os
import datetime
import time

filename = "output.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("Starting log\n")

while True:
    with open(filename, "a") as f:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{current_time}\n")
    time.sleep(60)