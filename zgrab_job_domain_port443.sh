#!/bin/bash
#Will also specify an out put file to make this easier for the scripts below as this will more than likely
#cause issues as all scripts are outputting two files
#~/fyp/final-year-project/zgrab_domain_port443.sh ~/fyp/final-year-project/ip_to_dns_1522089290/resolved_ip_to_dns1522089290.csv ~/fyp/final-year-project/zgrab_domain443scan.csv
~/fyp/final-year-project/zgrab_domain_port443.sh ~/fyp/final-year-project/not_alive_domain_443.csv ~/fyp/final-year-project/zgrab_domain443scan.csv
sed '1d' ~/fyp/final-year-project/zgrab_domain443scan.csv >> ~/fyp/final-year-project/zgrabDomain443ScanNoHeader.csv
rm -f summary_zgrab_*.txt
