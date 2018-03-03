#!/bin/bash
zmap -p 80 134.226.0.0/16 --output-fields=* -o 80scan.csv
zmap -p 443 134.226.0.0/16 --output-fields=* -o 443scan.csv
sed '1d' 80scan.csv > 80ScanNoHeader.csv
sed '1d' 443scan.csv > 443ScanNoHeader.csv
cat 80ScanNoHeader.csv 443ScanNoHeader.csv >> trinityIps.csv

