#!/bin/bash
#Will also specify an out put file to make this easier for the scripts below as this will more than likely
#cause issues as all scripts are outputting two files
~/fyp/final-year-project/zgrab_ip_port443_part2.sh ~/fyp/final-year-project/port_1522086307/port_443_part2.csv ~/fyp/final-year-project/zgrab_ip443scan_part2.csv
sed '1d' ~/fyp/final-year-project/zgrab_ip443scan_part2.csv >> ~/fyp/final-year-project/zgrabIp443ScanNoHeader_part2.csv
rm -f summary_zgrab_*.txt
