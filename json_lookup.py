#!/usr/bin/python3
import os
import sys
import csv
import time
import json
from datetime import datetime
from pprint import pprint
'''
#!/usr/bin/python3 (running in python 3) Will remove 'u' which is a unicode character

In production might swap over to jq instead, testing both methods?

'''


#the timestamp, in time_t format
now=str(int(time.time()))
str_now=str(datetime.now())


#if len(sys.argv)==2:
inputfile = sys.argv[1]

#if len(sys.argv)==3:
outputFile = sys.argv[2]

port = sys.argv[3]
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
if port == '443':
     try:
         issuer=data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['issuer']['common_name']
      #"['data'] ['http'] ['response'] ['request'] ['tls_handshake'] ['server_certificates'] ['certificate'] ['parsed'] ['validation_level']"
  except:
      issuer='False'

    try:
        subject_cn=['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['subject']['common_name']
    except:
        subject_cn ='False'
    try:
        secure_renegotiation =data['data']['http']['response']['request']['tls_handshake']['server_hello']['secure_renegotiation']
    except:
        secure_renegotiation ='False'

    try:
        tls_version_name =data['data']['http']['response']['request']['tls_handshake']['server_hello']['version']['name']
    except:
        tls_version_name ='False'


    try:
        self_signed =data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['signature']['self_signed']

    except:
        self_signed='False'
    try:
        certificate_names=data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['extensions']['subject_alt_name']['dns_names']
    except:
        certificate_names ='False'


    try:
        browser_trusted =data['data']['http']['response']['request']['tls_handshake']['server_certificates']['validation']['browser_trusted']

    except:
        browser_trusted ='False'

    try:
        cipher_suite = data['data']['http']['response']['request']['tls_handshake']['server_hello']['cipher_suite']['name']

    except:
        cipher_suite ='False'



try:
    cache_control =data['data']['http']['response']['headers']['cache_control']
except:
    cache_control ='False'

try:
    expires =data['data']['http']['response']['headers']['expires']
except:
    expires ='False'

try:
    pragma =data['data']['http']['response']['headers']['pragma']
except:
    pragma ='False'

try:
    connected =data['error']
except:
    connected ='True'

try:
    domain =data['domain']#.encode('utf8')
except:
    domain ='False'

try:
    ip =data['ip']#.encode('utf8')
except:
    ip ='False'

try:
    server =data['data']['http']['response']['headers']['server']
except:
    server ='False'

try:
    status_line =data['data']['http']['response']['status_line']
except:
    status_line='False'

try:
    location=data['data'] ['http'] ['response'] ['headers'] ['location']
except:
    location='False'


#Write results to csv file
if port == '443':
    with open(outputFile, "a") as myfile:
        writer=csv.writer(myfile)
        writer.writerow([domain,ip,connected,server,status_line,cache_control,expires,pragma,location,
        secure_renegotiation,tls_version_name,self_signed,certificate_names,browser_trusted,cipher_suite,issuer])

    
    myfile.close()
else:
    with open(outputFile, "a") as myfile1:
        writer1=csv.writer(myfile1)
        writer1.writerow([domain,ip,connected,server,status_line,cache_control,expires,pragma,location])


    myfile1.close()
#Print a flatten version of the json file
#pprint(flatten_json(data))
