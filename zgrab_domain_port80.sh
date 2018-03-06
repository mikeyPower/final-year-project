#!/bin/bash
#This script will run with a csv where the second column is domains
#./zgrab_domain_port80.sh file1


#Get time stamp
TIME_STAMP=$(date +%s)
touch zgrab_domain_p80_$TIME_STAMP.csv
touch zgrab_domain_summary_p80$TIME_STAMP.txt
echo "Domain,Ip,Connected,Server,Status Line,Cache Control,Expires,Pragma,Location" >> zgrab_domain_p80_$TIME_STAMP.csv

#Outputs of banner grabs will be outputted to /go/src/github.com/zmap/zgrab directory

#Could echo the port number depending on the file e.g. echo "${b[0]}"
sed 1d $1

while IFS=, read -a b;
do

    (cd ~/go/src/github.com/zmap/zgrab && echo "${b[1]}" | ./zgrab --port 80 --http="/" --lookup-domain --output-file=banners.json)

  #  (cd ~/go/src/github.com/zmap/zgrab && cat banners.json | jq '.data.http.response.request.tls_handshake.server_certificates.chain[1].raw', 'Stuff'>> summary_TIME_STAMP.csv)
                #  OR
    ./json_lookup.py ~/go/src/github.com/zmap/zgrab/banners.json zgrab_domain_p80_$TIME_STAMP.csv 80
    sleep .2
done < sed 1d $1 #removing header line

#Summary results
echo 'Ran zgrab_domain.sh at '+ $TIME_STAMP >> zgrab_domain_summary_p80_$TIME_STAMP.txt
echo 'Input file: ' >> zgrab_domain_summary_p80_$TIME_STAMP.txt
echo "$1" >> zgrab_domain_summary_p80_$TIME_STAMP.txt
echo "Files created:" >> zgrab_domain_summary_p80_$TIME_STAMP.txt
echo 'zgrab_domain_p80_'$TIME_STAMP'.csv' >> zgrab_domain_summary_p80_$TIME_STAMP.txt
