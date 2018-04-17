#!/bin/bash
#This script will run with a csv where the second column is domains
#./zgrab_domain_port443.sh file1


#Get time stamp
TIME_STAMP=$(date +%s)
#touch zgrab_domain_p443_$TIME_STAMP.csv
touch summary_zgrab_domain_p443_$TIME_STAMP.txt
echo "Time,Domain,Ip,Port,Connected,Server,Status Line,Cache Control,Header Expires,Pragma,\
Location,Secure Regotitation,TlS Version,Self Signed,Subject Common Name,Certificate Alt Names,\
Browser Trusted,Cipher,Issuer,Matches Domain,Cert Start,Cert End,Cert Validity Length,Cert Expired,Public Key,\
Public Key Length,Signature Algorithm,Key Algorithm,Curve Id,Compression Method,Body" > $2

#Outputs of banner grabs will be outputted to /go/src/github.com/zmap/zgrab directory

#Could echo the port number depending on the file e.g. echo "${b[0]}"
sed 1d $1 > ~/fyp/final-year-project/input2.csv
while IFS=, read -a b;
do

    (cd ~/go/src/github.com/zmap/zgrab && echo "${b[2]}" | ./zgrab --port 443 --tls --http="/" --lookup-domain --timeout 4 --output-file=banners2.json)

    ~/fyp/final-year-project/json_lookup.py ~/go/src/github.com/zmap/zgrab/banners2.json $2 443 ${b[1]}


done < ~/fyp/final-year-project/input2.csv #removing header line

#Summary results
echo 'Ran zgrab_domain.sh at '$(date -d @$TIME_STAMP +"%d-%m-%Y %T") >> summary_zgrab_domain_p443_$TIME_STAMP.txt
echo 'Input file: ' >> summary_zgrab_domain_p443_$TIME_STAMP.txt
echo "$1" >> summary_zgrab_domain_p443_$TIME_STAMP.txt
echo "Files created: " >> summary_zgrab_domain_p443_$TIME_STAMP.txt
echo $2 >> summary_zgrab_domain_p443_$TIME_STAMP.txt
