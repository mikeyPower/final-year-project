#!/bin/bash
#Will also specify an out put file to make this easier for the scripts below as this will more than likely
#cause issues as all scripts are outputting two files
./zgrab_domain_port443.sh safe-list.csv.test zgrab_domain443scan.csv
sed '1d' zgrab_domain443scan.csv >> zgrabDomain443ScanNoHeader.csv
rm -f summary_zgrab_*.txt
