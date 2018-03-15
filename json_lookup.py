#!/usr/bin/python3
import os
import sys
import csv
import time
import json
from datetime import datetime
from pprint import pprint
#from Crypto.PublicKey.RSA import construct
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


 #"['data'] ['http'] ['response'] ['request'] ['tls_handshake'] ['server_key_exchange'] ['ecdh_params'] ['curve_id'] ['name']": 'secp256r1',







if port == '443':
    try:
        curve_id=data['data']['http'] ['response']['request']['tls_handshake']['server_key_exchange']['ecdh_params']['curve_id']['id']
    except:
        curve_id='Not Present'



    try:
        matches_domain=data['data']['http']['response']['request']['tls_handshake']['server_certificates']['validation']['matches_domain']
    except:
        matches_domain='Not Present'

    try:
        cert_start=data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['validity']['start']
    except:
        cert_start='Not Present'


    try:
        # Need to check if the certificate is out of date 
        cert_end=data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['validity']['end']
    except:
        cert_end='Not Present'

    try:
        cert_validity_length=data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['validity']['length'] #in seconds
    except:
        cert_validity_length='Not Present'



    try:
        pk_length=data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['subject_key_info']['rsa_public_key']['length']
    except:
        pk_length='Not Present'


    try:
        key_algorithm=data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['subject_key_info']['key_algorithm']['name']
    except:
        key_algorithm='Not Present'

    try:
        public_key=data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['subject_key_info']['fingerprint_sha256']
    except:
        public_key='Not Present'



    try:
        signature_algorithm=data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['signature']['signature_algorithm']['name']
    except:
        signature_algorithm='Not Present'





    try:

        cert = data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['raw']
        formatCert =cert
        #cert_f="cert_raw.crt"
        #cert_file=open(cert_f,"w")
        #cert_file.write('-----BEGIN CERTIFICATE-----\n')
        #cert_file.write(formatCert+'\n')
        #cert_file.write('-----END CERTIFICATE-----\n')
        #cert_file.close()

        #print(formatCert)

    except:
        cert ='Not Present'
    try:
        issuer=data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['issuer']['common_name']
      #"['data'] ['http'] ['response'] ['request'] ['tls_handshake'] ['server_certificates'] ['certificate'] ['parsed'] ['validation_level']"
    except:
        issuer='Not Present'

    try:

        subject_cn=data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['subject']['common_name']
    except:
        subject_cn ='Not Present'
    try:
        secure_renegotiation =data['data']['http']['response']['request']['tls_handshake']['server_hello']['secure_renegotiation']
    except:
        secure_renegotiation ='Not Present'

    try:
        tls_version_name =data['data']['http']['response']['request']['tls_handshake']['server_hello']['version']['name']
    except:
        tls_version_name ='Not Present'


    try:
        self_signed =data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['signature']['self_signed']

    except:
        self_signed='Not Present'
    try:
        certificate_names=data['data']['http']['response']['request']['tls_handshake']['server_certificates']['certificate']['parsed']['extensions']['subject_alt_name']['dns_names']
    except:
        certificate_names ='Not Present'


    try:
        browser_trusted =data['data']['http']['response']['request']['tls_handshake']['server_certificates']['validation']['browser_trusted']

    except:
        browser_trusted ='Not Present'

    try:
        cipher_suite = data['data']['http']['response']['request']['tls_handshake']['server_hello']['cipher_suite']['name']

    except:
        cipher_suite ='Not Present'



try:
    cache_control =data['data']['http']['response']['headers']['cache_control']
except:
    cache_control ='Not Present'

try:
    expires =data['data']['http']['response']['headers']['expires']
except:
    expires ='Not Present'

try:
    pragma =data['data']['http']['response']['headers']['pragma']
except:
    pragma ='Not Present'

try:
    connected =data['error']
except:
    connected ='True'

try:
    domain =data['domain']#.encode('utf8')
except:
    domain ='Not Present'

try:
    ip =data['ip']#.encode('utf8')
except:
    ip ='Not Present'

try:
    server =data['data']['http']['response']['headers']['server']
except:
    server ='Not Present'

try:
    status_line =data['data']['http']['response']['status_line']
except:
    status_line='Not Present'

try:
    location=data['data'] ['http'] ['response'] ['headers'] ['location']
except:
    location='Not Present'


#Write results to csv file
if port == '443':
    with open(outputFile, "a") as myfile:
        writer=csv.writer(myfile)
        writer.writerow([domain,ip,connected,server,status_line,cache_control,expires,pragma,location,
        secure_renegotiation,tls_version_name,self_signed,subject_cn,certificate_names,browser_trusted,cipher_suite,issuer,
        matches_domain,cert_start,cert_end,cert_validity_length,public_key,pk_length,signature_algorithm,key_algorithm,curve_id])


    myfile.close()
else:
    with open(outputFile, "a") as myfile1:
        writer1=csv.writer(myfile1)
        writer1.writerow([domain,ip,connected,server,status_line,cache_control,expires,pragma,location])


    myfile1.close()
#Print a flatten version of the json file
#pprint(flatten_json(data))
