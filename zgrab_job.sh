#!/bin/bash
#Will also specify an out put file to make this easier for the scripts below as this will more than likely
#cause issues as all scripts are outputting two files
./zgrab_domain_port80.sh safe-list.csv.test zgrab_domain80scan.csv
./zgrab_domain_port443.sh safe-list.csv.test zgrab_domain443scan.csv
./zgrab_ip_port80.sh safe-list.csv.test zgrab_ip80scan.csv
./zgrab_ip_port443.sh safe-list.csv.test zgrab_ip443scan.csv
sed '1d' zgrab_domain80scan.csv >> zgrabDomain80ScanNoHeader.csv
sed '1d' zgrab_domain443scan.csv >> zgrabDomain443ScanNoHeader.csv
sed '1d' zgrab_ip80scan.csv >> zgrabIp80ScanNoHeader.csv
sed '1d' zgrab_ip443scan.csv >> zgrabIp443ScanNoHeader.csv
rm -f summary_zgrab_*.txt
