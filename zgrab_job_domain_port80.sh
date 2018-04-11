#!/bin/bash
#Will also specify an out put file to make this easier for the scripts below as this will more than likely
#cause issues as all scripts are outputting two files
~/fyp/final-year-project/zgrab_domain_port80.sh ~/fyp/final-year-project/ip_to_dns_1522088570/resolved_ip_to_dns1522088570.csv ~/fyp/final-year-project/zgrab_domain80scan.csv
#~/fyp/final-year-project/zgrab_domain_port80.sh ~/fyp/final-year-project/not_alive_domain_80.csv ~/fyp/final-year-project/zgrab_domain80scan.csv
sed '1d' ~/fyp/final-year-project/zgrab_domain80scan.csv >> ~/fyp/final-year-project/zgrabDomain80ScanNoHeader.csv
rm -f summary_zgrab_*.txt
