#!/bin/bash
#cat tmp.csv |./zgrab_domain.sh (i.e. pipe file to script)

#Get time stamp
TIME_STAMP=$(date +%s)
touch summary_TIME_STAMP.csv
echo "Header" >> summary_TIME_STAMP.csv


#Outputs of banner grabs will be outputted to /go/src/github.com/zmap/zgrab directory
while IFS=, read -a b;
do
    #echo "${b[0]}" | ./zgrab --port 443 --tls --http="/" --lookup-domain --output-file=banners.json

    (cd ~/go/src/github.com/zmap/zgrab && echo "${b[0]}" | ./zgrab --port 443 --tls --lookup-domain --output-file=banners.json)

    (cd ~/go/src/github.com/zmap/zgrab && cat banners.json | jq '.data.http.response.request.tls_handshake.server_certificates.chain[1].raw', 'Stuff'>> summary_TIME_STAMP.csv)
                #  OR
    ./json_lookup.py ~/go/src/github.com/zmap/zgrab/banners.json
    sleep .1
done #<tmp.csv
