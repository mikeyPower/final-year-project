#!/bin/bash

# make a 100 record test file

FILE=TrinityIps.csv
OFILE=100recs.csv

head -8000 $FILE | tail -50 >$OFILE
head -18000 $FILE | tail -49 >>$OFILE
tail -1 $FILE >>$OFILE
