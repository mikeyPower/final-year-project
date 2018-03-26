#!/bin/bash
#This script will run with a csv where the second column is domains
#./zgrab_domain_port80.sh file1


#Get time stamp
TIME_STAMP=$(date +%s)
#touch zgrab_domain_p80_$TIME_STAMP.csv
touch summary_zgrab_domain_p80_$TIME_STAMP.txt
echo "Time,Domain,Ip,Port,Connected,Server,Status Line,Cache Control,Header Expires,Pragma,Location" > $2

#Outputs of banner grabs will be outputted to /go/src/github.com/zmap/zgrab directory

#Could echo the port number depending on the file e.g. echo "${b[0]}"
sed 1d $1 > input.csv
while IFS=, read -a b;
do

    (cd ~/go/src/github.com/zmap/zgrab && echo "${b[2]}" | ./zgrab --port 80 --http="/" --lookup-domain --timeout 5 --output-file=banners.json)

  #  (cd ~/go/src/github.com/zmap/zgrab && cat banners.json | jq '.data.http.response.request.tls_handshake.server_certificates.chain[1].raw', 'Stuff'>> summary_TIME_STAMP.csv)
                #  OR
    ./json_lookup.py ~/go/src/github.com/zmap/zgrab/banners.json $2 80 ${b[1]}

done < input.csv #removing header line

#Summary results
echo 'Ran zgrab_domain.sh at '$(date -d @$TIME_STAMP +"%d-%m-%Y %T") >> summary_zgrab_domain_p80_$TIME_STAMP.txt
echo 'Input file: ' >> summary_zgrab_domain_p80_$TIME_STAMP.txt
echo "$1" >> summary_zgrab_domain_p80_$TIME_STAMP.txt
echo "Files created:" >> summary_zgrab_domain_p80_$TIME_STAMP.txt
echo $2 >> summary_zgrab_domain_p80_$TIME_STAMP.txt
