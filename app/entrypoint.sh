#!/bin/bash

OUTFILE=output.txt

service ssh start

while [ true ]; do
    date +'%F %T' >> ${OUTFILE}
    sleep 60
done