#!/bin/bash
#Will also specify an out put file to make this easier for the scripts below as this will more than likely
#cause issues as all scripts are outputting two files
~/fyp/final-year-project/zgrab_ip_port80.sh ~/fyp/final-year-project/port_1522086307/port_80_part1.csv ~/fyp/final-year-project/zgrab_ip80scan.csv
#~/fyp/final-year-project/zgrab_ip_port80.sh ~/fyp/final-year-project/not_alive_ip_80.csv ~/fyp/final-year-project/zgrab_ip80scan.csv
sed '1d' ~/fyp/final-year-project/zgrab_ip80scan.csv >> ~/fyp/final-year-project/zgrabIp80ScanNoHeader.csv
rm -f summary_zgrab_*.txt
