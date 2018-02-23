#cat tmp.csv |./zgrab_domain.sh pipe file to script


while IFS=, read -a b;
do
    echo "${b[0]}" | ./zgrab --port 443 --tls --http="/" --lookup-domain --output-file=banners.json
    #echo "www.tcd.ie"
done #<tmp.csv
