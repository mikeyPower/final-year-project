#!/bin/bash
#This script will run with a csv where the first column is ip


#Get time stamp
TIME_STAMP=$(date +%s)
touch zgrab_ip_p443_$TIME_STAMP.csv

touch zgrab_ip_p443_summary_$TIME_STAMP.txt

echo "Domain,Ip,Connected,Server,Status Line,Cache Control,Header Expires,Pragma,Location,\
Secure Regotitation,TlS Version,Self Signed,Subject Common Name,Certificate Alt Names,Browser Trusted,\
Cipher,Issuer,Matches Domain,Cert Start,Cert End,Cert Validity Length,Public Key,Public Key Length,\
Signature Algorithm,Key Algorithm,Curve Id" >> zgrab_ip_p443_$TIME_STAMP.csv

#Outputs of banner grabs will be outputted to /go/src/github.com/zmap/zgrab directory


#Could echo the port number depending on the file e.g. echo "${b[0]}"
sed 1d $1 > input.csv
while IFS=, read -a b;
do

    (cd ~/go/src/github.com/zmap/zgrab && echo "${b[0]}" | ./zgrab --port 443 --tls --http="/" --output-file=banners.json)

    ./json_lookup.py ~/go/src/github.com/zmap/zgrab/banners.json zgrab_ip_p443_$TIME_STAMP.csv 443

done < input.csv #removing header line

#Summary results
echo 'Ran zgrab_domain.sh at '+ $TIME_STAMP >> zgrab_ip_p443_summary_$TIME_STAMP.txt
echo 'Input file: ' >> zgrab_ip_p443_summary_$TIME_STAMP.txt
echo "$1" >> zgrab_ip_p443_summary_$TIME_STAMP.txt
echo "Files created:" >> zgrab_ip_p443_summary_$TIME_STAMP.txt
echo 'zgrab_domain_port443_'$TIME_STAMP'.csv' >> zgrab_ip_p443_summary_$TIME_STAMP.txt
