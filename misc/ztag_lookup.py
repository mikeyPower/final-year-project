#!/usr/bin/python3
#import dns.resolver
import os
import sys
import csv
import time
import json
from datetime import datetime
import dateutil.parser
from pprint import pprint
import socket
#from Crypto.PublicKey.RSA import construct
'''
#!/usr/bin/python3 (running in python 3) Will remove 'u' which is a unicode character

In production might swap over to jq instead, testing both methods?

'''


#the timestamp, in time_t format
now=str(int(time.time()))
str_now=str(datetime.now())

#create directory for outputted results
#try:
#   os.makedirs('html_pages')
#except OSError:
#    if not os.path.isdir(path):
#        raise



#if len(sys.argv)==2:
inputfile = sys.argv[1]

#if len(sys.argv)==3:
outputFile = sys.argv[2]

ports = sys.argv[3]

#print(str(sys.argv[4]))
'''
if not os.path.isfile(file) or not os.access(file,os.R_OK):
    print"Can't read input file: " + file + " - exiting"
    sys.exit(1)
'''
with open(inputfile,'r') as json_file:
    data = json.load(json_file)
    #data = ast.literal_eval(json.dumps(data)) #removes unicode character from output


#Flatten Json as  would be accessible if indexing a dictionary
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + '['+"'"+a +"'"+ ']'+' ')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + '['+"'"+ str(i)+"'"+']' +' ')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out










try:
    title=data['title']
except:
    title='Not Present'
try:
    status_line=data['status_line']
except:
    status_line='Not Present'

try:
    tags=data['tags']
except:
    tags='Not Present'

try:
    timestamp=data['timestamp']
except:
    timestamp='Not Present'


try:
    body=data['body_sha256']
except:
    body='Not Present'

try:
    content_type =data['headers']['content_type']
except:
    content_type ='Not Present'

try:
    server =data['headers']['server']
except:
    server ='Not Present'

try:
    key =data['headers']['unknown'][0]['key']
except:
    key ='Not Present'

try:
    value =data['headers']['unknown'][0]['value']
except:
    value ='True'

try:
    domain =data['domain']#.encode('utf8')
except:
    domain ='Not Present'

try:
    ip =data['ip_address']
except:
    ip ='Not Present'

try:
    x_ua_compatible =data['headers']['x_ua_compatible']

except:
    x_ua_compatible ='Not Present'


try:
    description=data['local_metadata']['description']
except:
    description='Not Present'



try:
    manufacturer=data['local_metadata']['manufacturer']
except:
    manufacturer='Not Present'


try:
    product=data['local_metadata']['product']
except:
    product='Not Present'


try:
    version=data['local_metadata']['version']
except:
    version='Not Present'


try:
    status_code=data['status_code']
except:
    status_code='Not Present'


if domain == 'Not Present':
    try:
        #works in python 2 but not in python3 dash still missing will try other dns resolver
        #print(ip)
        rdns=socket.gethostbyaddr(ip)
        domain =str(rdns[0])
        #test = domain.encode('utf-8')
        #print(test)
        #print(str(rdns[0]))
        #print(rdns)
        #print(domain)


        #req = '.'.join(reversed(ip.split("."))) + ".in-addr.arpa"
        #answers = dns.resolver.query(req, "PTR")
        #print(answers[0])
    except:
        domain="unresolved"


if ip == '<nil>':
    try:
        ipdns=socket.gethostbyname(domain)
        ip=str(ipdns)
    except:
        ip == 'unresolved'


#Write results to csv file

with open(outputFile, "a") as myfile:

    writer=csv.writer(myfile)
    writer.writerow([timestamp,domain,ip,ports,content_type,server,key,value,x_ua_compatible,description,manufacturer,product,version,status_code,status_line,tags,title])

myfile.close()

#Print a flatten version of the json file
#pprint(flatten_json(data))
