#!/bin/bash
#This script will run with a csv where the first column is domains
#./zgrab_domain_port443.sh file1


#Get time stamp
TIME_STAMP=$(date +%s)
touch zgrab_domain_p443_$TIME_STAMP.csv
_
touch zgrab_domain_summary_p443_$TIME_STAMP.txt
echo "Domain,Ip,Connected,Server,Status Line,Cache Control,Expires,Pragma,Location,Secure Regotitation,TlS Version,Self Signed,Certificate Names,Browser Trusted,Cipher,Issuer" >> zgrab_domain_p443_$TIME_STAMP.csv

#Outputs of banner grabs will be outputted to /go/src/github.com/zmap/zgrab directory

#Might have to remove header file from csv before piping it through
#Could echo the port number depending on the file e.g. echo "${b[0]}"
while IFS=, read -a b;
do

    (cd ~/go/src/github.com/zmap/zgrab && echo "${b[1]}" | ./zgrab --port 443 --tls --http="/" --lookup-domain --output-file=banners.json)

    ./json_lookup.py ~/go/src/github.com/zmap/zgrab/banners.json zgrab_domain_p443_$TIME_STAMP.csv 443
    sleep .2
done < $1

#Summary results
echo 'Ran zgrab_domain.sh at '+ $TIME_STAMP >> zgrab_domain_summary_p443_$TIME_STAMP.txt
echo 'Input file: ' >> zgrab_domain_summary_p443_$TIME_STAMP.txt
echo "$1" >> zgrab_domain_summary_p443_$TIME_STAMP.txt
echo "Files created: " >> zgrab_domain_summary_p443_$TIME_STAMP.txt
echo 'zgrab_domain_p443_TIME_STAMP.csv' >> zgrab_domain_summary_p443_$TIME_STAMP.txt
