# final-year-project

## Things to do

1. will add options to output results to csv file

2. Requirements doc (prerequisites for running programmes)

3. Need to also make sure data is not being duplicated

## Setting up Cron Job
Ensure Path is included in order for cron environment to be same as user environment in order to run zmap

    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games

    0 * * * * /home/usr/zmap_job.sh

## Pretty Print Json to terminal
    python -m json.tool input.json

    cat input.json | jq '.'

## Show all paths in json
[links](https://github.com/stedolan/jq/issues/243)

    jq -c 'path(..)|[.[]|tostring]|join("/")' banners_test.json

    jq 'path(..)' banners_test.json


## Organnising Ips according port numbers
Example:           

    ./port.py zmap.csv (Input is the original csv file outputted by zmap)

Output:


     port_443_TIME_STAMP.csv (csv file contains ip and port number)

     port_80_TIME_STAMP.csv  (csv file contains ip and port number)

     both_ports_TIME_STAMP.csv (csv file contains ip listenning on both ports)

     summary_ports_TIME_STAMP.txt (Summary report of programme run)

     --MIGHT ALSO OUTPUT ALL UNIQUE IPS IN ORDER TO INPUT ALL IPS TO REVERSE DNS LOOKUP--

## Reverse DNS lookup
Example:

     ./ip_to_dns.py input.csv (Input is a csv file of ips where the first column are ips and second column is port number(s))
Output:   

    resolved_ip_to_dns_TIME_STAMP.csv (HEADER = 'Queried Ip','Port','Hostname', 'alias-list', 'Ip')

    unresolved_ip_to_dns_TIME_STAMP.csv (HEADER = 'Queried Ip','Port','Error')

    multiple_ip_to_dns_TIME_STAMP.csv (HEADER = 'DNS','IP list')

    summary_dns_TIME_STAMP.txt (Summary reprt of programme run)

    --MIGHT REMOVE PORT NUMBER OUTPUT AT THIS STAGE IN PROGRAMME RUN--

## Extracting data from Json
Example:

first parameter = json produced from zgrab


second parameter = output file

third parameter = port number of inputed domains/ips



     ./json_lookup.py ~/go/src/github.com/zmap/zgrab/banners.json   zgrab_domain_port443_$TIME_STAMP.csv 443


Output:

    --TO BE DONE--summary results

