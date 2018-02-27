#!/bin/bash
#This script will run with a list of domain names on port 443
#cat tmp.csv |./zgrab_domain.sh (i.e. pipe file to script)

#Get time stamp
TIME_STAMP=$(date +%s)
touch zgrab_domain_port443_$TIME_STAMP.csv
echo "Domain,Connected,Server,Status Line,Secure Regotitation,TlS Version,Self Signed,Certificate Names,Browser Trusted,Cipher" >> zgrab_domain_port443_$TIME_STAMP.csv

#Outputs of banner grabs will be outputted to /go/src/github.com/zmap/zgrab directory
while IFS=, read -a b;
do

    (cd ~/go/src/github.com/zmap/zgrab && echo "${b[0]}" | ./zgrab --port 443 --tls --http="/" --lookup-domain --output-file=banners.json)

  #  (cd ~/go/src/github.com/zmap/zgrab && cat banners.json | jq '.data.http.response.request.tls_handshake.server_certificates.chain[1].raw', 'Stuff'>> summary_TIME_STAMP.csv)
                #  OR
    ./json_lookup.py ~/go/src/github.com/zmap/zgrab/banners.json zgrab_domain_port443_$TIME_STAMP.csv #will open json_test_with_domain_port443_TIME_STAMP.csv in json_lookup.py and results to this
    sleep .1
done #<tmp.csv

#Summary results
touch zgrab_domain_port443_summary_$TIME_STAMP.txt
echo 'Ran zgrab_domain.sh at '+ $TIME_STAMP >> zgrab_domain_port443_summary_$TIME_STAMP.txt
echo "Files created:" >> zgrab_domain_port443_summary_$TIME_STAMP.txt
echo 'json_test_with_domain_port443_TIME_STAMP.csv' >> zgrab_domain_port443_summary_$TIME_STAMP.txt
