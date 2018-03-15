# final-year-project

## Things to do

1. will add options to output results to csv file

2. Requirements doc (prerequisites for running programmes)


## Setting up Cron Job
Ensure environment path is included in order for cron environment to be same as user environment to successfully run zmap

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
### Example:           
 Input is the original csv file outputted by zmap

    ./port.py zmap.csv

### Output:
Four files are outputted from the execution above they are as follows all ips on port 443, ips on port 80, ips on both ports, summary report of programme execution as well as all unique ips  


     port_443_TIME_STAMP.csv (HEADER = 'IP','PORT')

     port_80_TIME_STAMP.csv  (HEADER = Ip,Port)

     both_ports_TIME_STAMP.csv (HEADER = Ip,Port)

     summary_ports_TIME_STAMP.txt (Summary report of programme run)

     all_ip_ports_TIME_STAMP.csv (HEADER = Ip,Port)

## Reverse DNS lookup
### Example:
Input is a csv file where the first column are ips and second column is port number(s)

     ./ip_to_dns.py input.csv
### Output:   

Four files are outputted from the execution above, they are as follows a csv file containing all ips that resolved to dns, those that haven't resolved to dns, those who dns have multiple ip's as well as a summary report of programme execution

    resolved_ip_to_dns_TIME_STAMP.csv (HEADER = Queried Ip,Port,Hostname,alias-list, Ip)

    unresolved_ip_to_dns_TIME_STAMP.csv (HEADER = Queried Ip,Port,Error)

    multiple_ip_to_dns_TIME_STAMP.csv (HEADER = DNS,IP list)

    summary_dns_TIME_STAMP.txt (Summary report of programme run)


## Extracting data from Json
### Example:

first parameter = json produced from zgrab


second parameter = output file

third parameter = port number of inputed domains/ips (Default port 80)



     ./json_lookup.py ~/go/src/github.com/zmap/zgrab/banners.json   zgrab_domain_port443_$TIME_STAMP.csv 443


### Output:

   appends the results to the second input with the relevant results depending on the port number chosen



## Scripts for ZGrab Execution
### Domain Input:

    ./zgrab_domain_port80.sh <domain_input.csv>
    ./zgrab_domain_port443.sh <domain_input.csv>
The above two scripts take their input from the reverse dns lookup or a csv file where the third column is a domain name

Each script specifies the port that the zgrab will be conducted on

The <input.csv> is simply looped through every time piping a domain to zgrab

The json file outputed from the zgrab will be piped into the

    ./json_lookup.py <zgrab_result.json> <output.csv> <port number>

The results from above are appended to the output.csv

this will continue until we've reached the last domain in the csv file

### Ip input:

    ./zgrab_ip_port80.sh <ip_input.csv>
    ./zgrab_ip_port443.sh <ip_input.csv>
The above two scripts take their input from the reverse dns lookup or a csv file where the first  column is an ip address

Each script specifies the port that the zgrab will be conducted on

The <input.csv> is simply looped through every time piping an ip address to zgrab

Then the json file outputed from the zgrab will be piped into the below programme

    ./json_lookup.py <zgrab_result.json> <output.csv> <port number>

The results from the above are appended to the output.csv

This will continue until we've reached the last Ip address in the csv file

### Output:
   Each script produces two files, which are a csv file containing the information parsed from the zgrab as well as a summary report of the programme execution

     zgrab_domain_p80_TIME_STAMP.csv (HEADER = Domain,Ip,Connected,Server,Status Line,CacheControl,Header Expires,Pragma,Location)
     zgrab_domain_summary_p80_TIME_STAMP.txt


### Filtering:
To filter the data taken from any of the above scripts dealing with ZGrab, the programme below will take a csv file, keyword 'ip' or 'domain' and port number 443 or 80

    ./zgrab_parse.py zgrab_domain_p433_*.csv domain 443

### Output:
--TO BE DONE--
