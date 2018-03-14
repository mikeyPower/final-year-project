#!/bin/bash
#This script will run with a csv where the first column is ip
#./zgrab_ip_port80.sh file1


#Get time stamp
TIME_STAMP=$(date +%s)
touch zgrab_ip_p80_$TIME_STAMP.csv
touch zgrab_ip_p80_summary_$TIME_STAMP.txt
echo "Domain,Ip,Connected,Server,Status Line,Cache Control,Header Expires,Pragma,Location" >> zgrab_ip_p80_$TIME_STAMP.csv

#Outputs of banner grabs will be outputted to /go/src/github.com/zmap/zgrab directory

#Could echo the port number depending on the file e.g. echo "${b[0]}"
sed 1d $1 > input.csv
while IFS=, read -a b;
do

    (cd ~/go/src/github.com/zmap/zgrab && echo "${b[0]}" | ./zgrab --port 80 --http="/" --output-file=banners.json)

  #  (cd ~/go/src/github.com/zmap/zgrab && cat banners.json | jq '.data.http.response.request.tls_handshake.server_certificates.chain[1].raw', 'Stuff'>> summary_TIME_STAMP.csv)
                #  OR
    ./json_lookup.py ~/go/src/github.com/zmap/zgrab/banners.json zgrab_ip_p80_$TIME_STAMP.csv 80
    sleep .2
done < input.csv #removing header line

#Summary results
echo 'Ran zgrab_domain.sh at '+ $TIME_STAMP >> zgrab_ip_p80_summary_$TIME_STAMP.txt
echo 'Input file: ' >> zgrab_ip_p80_summary_$TIME_STAMP.txt
echo "$1" >> zgrab_ip_p80_summary_$TIME_STAMP.txt
echo "Files created:" >> zgrab_ip_p80_summary_$TIME_STAMP.txt
echo 'zgrab_ip_port80_'$TIME_STAMP'.csv' >> zgrab_ip_p80_summary_$TIME_STAMP.txt
