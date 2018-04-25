#!/usr/bin/python
import csv
import sys
from functions import dateRange
from datetime import datetime
import time
import os

#Get timestamp of programme execution
now=str(int(time.time()))
str_now=str(datetime.now())

csvFile = sys.argv[1]

csv.field_size_limit(sys.maxsize)
#create directory for outputted results
try:
    os.makedirs('zgrab_parse_'+now)
except OSError:
    if not os.path.isdir(path):
        raise


if sys.argv[2] == 'domain':
    ipDomain = 1
    legend ='Domain'
else:
    ipDomain =2
    legend ='Ip'


if sys.argv[3] == '443':
    port = 443
else:
    port =80



timeField=0
domainField =1
ipField=2
portField=3
connectedField=4
serverField=5
statusLineField=6
cacheControlField=7
headerExpiresField=8
pragmaField=9
locationField=10
secureRecognitionField=11
tlSVersionField=12
selfSignedField=13
subjectCommonNameField=14
certificateAltNamesField=15
browserTrustedField=16
cipherField=17
issuerField=18
matchesDomainField=19
certStartField=20
certEndField=21
certValidityLengthField=22
certExpiredField=23
publicKeyField=24
publicKeyLengthField=25
signatureAlgorithmField=26
keyAlgorithmField=27
curveIdField=28
compressionMethodField=29

ipsDomains=[]
dictionaryPk={}
statusCode={}
secureRegotitation={}
tls={}
selfSigned={}
browserTrusted={}
cipherSuite={}
keyAlgorithm ={}
signatureAlgorithm={}
pKLength ={}
curveId={}
compressionMethod={}
server ={}
cacheControl={}
headerExpires={}
pragma={}
location={}

with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    readCSV.next() #Skip first line (Header line)

    for i in readCSV:

        #ensure where not checking duplicates
        if i[ipDomain] not in ipsDomains:


            ipsDomains.append(i[ipDomain])
            if port == 443:

                if (i[publicKeyField] in dictionaryPk) and (i[ipDomain] not in dictionaryPk[i[publicKeyField]]):
                    dictionaryPk[i[publicKeyField]].append(i[ipDomain])
                elif i[publicKeyField] not in dictionaryPk:
                    dictionaryPk[i[publicKeyField]] = [i[ipDomain]]


                if (i[secureRecognitionField] in secureRegotitation) and (i[ipDomain] not in secureRegotitation[i[secureRecognitionField]]):
                    secureRegotitation[i[secureRecognitionField]].append(i[ipDomain])
                elif i[secureRecognitionField] not in secureRegotitation:
                    secureRegotitation[i[secureRecognitionField]] = [i[ipDomain]]


                if (i[tlSVersionField] in tls) and (i[ipDomain] not in tls[i[tlSVersionField]]):
                    tls[i[tlSVersionField]].append(i[ipDomain])
                elif i[tlSVersionField] not in tls:
                    tls[i[tlSVersionField]] = [i[ipDomain]]

                if (i[selfSignedField] in selfSigned) and (i[ipDomain] not in selfSigned[i[selfSignedField]]):
                    selfSigned[i[selfSignedField]].append(i[ipDomain])
                elif i[selfSignedField] not in selfSigned:
                    selfSigned[i[selfSignedField]] = [i[ipDomain]]



                if (i[browserTrustedField] in browserTrusted) and (i[ipDomain] not in browserTrusted[i[browserTrustedField]]):
                    browserTrusted[i[browserTrustedField]].append(i[ipDomain])
                elif i[browserTrustedField] not in browserTrusted:
                    browserTrusted[i[browserTrustedField]] = [i[ipDomain]]


                if (i[cipherField] in cipherSuite) and (i[ipDomain] not in cipherSuite[i[cipherField]]):
                    cipherSuite[i[cipherField]].append(i[ipDomain])
                elif i[cipherField] not in cipherSuite:
                    cipherSuite[i[cipherField]] = [i[ipDomain]]

                if (i[curveIdField] in curveId) and (i[ipDomain] not in curveId[i[curveIdField]]):
                    curveId[i[curveIdField]].append(i[ipDomain])
                elif i[curveIdField] not in curveId:
                    curveId[i[curveIdField]] = [i[ipDomain]]


                if (i[keyAlgorithmField] in keyAlgorithm) and (i[ipDomain] not in keyAlgorithm[i[keyAlgorithmField]]):
                    keyAlgorithm[i[keyAlgorithmField]].append(i[ipDomain])
                elif i[keyAlgorithmField] not in keyAlgorithm:
                    keyAlgorithm[i[keyAlgorithmField]] = [i[ipDomain]]


                if (i[signatureAlgorithmField] in signatureAlgorithm) and (i[ipDomain] not in signatureAlgorithm[i[signatureAlgorithmField]]):
                    signatureAlgorithm[i[signatureAlgorithmField]].append(i[ipDomain])
                elif i[signatureAlgorithmField] not in signatureAlgorithm:
                    signatureAlgorithm[i[signatureAlgorithmField]] = [i[ipDomain]]

                if (i[publicKeyLengthField] in pKLength) and (i[ipDomain] not in pKLength[i[publicKeyLengthField]]):
                    pKLength[i[publicKeyLengthField]].append(i[ipDomain])
                elif i[publicKeyLengthField] not in pKLength:
                    pKLength[i[publicKeyLengthField]] = [i[ipDomain]]

                if (i[compressionMethodField] in compressionMethod) and (i[ipDomain] not in compressionMethod[i[compressionMethodField]]):
                    compressionMethod[i[compressionMethodField]].append(i[ipDomain])
                elif i[compressionMethodField] not in compressionMethod:
                    compressionMethod[i[compressionMethodField]] = [i[ipDomain]]

            if (i[serverField] in server) and (i[ipDomain] not in server[i[serverField]]):
                server[i[serverField]].append(i[ipDomain])
            elif i[serverField] not in server:
                server[i[serverField]] = [i[ipDomain]]


            if (i[statusLineField] in statusCode) and (i[ipDomain] not in statusCode[i[statusLineField]]):
                statusCode[i[statusLineField]].append(i[ipDomain])
            elif i[statusLineField] not in statusCode:
                statusCode[i[statusLineField]] = [i[ipDomain]]



            if (i[cacheControlField] in cacheControl) and (i[ipDomain] not in cacheControl[i[cacheControlField]]):
                cacheControl[i[cacheControlField]].append(i[ipDomain])
            elif i[cacheControlField] not in cacheControl:
                cacheControl[i[cacheControlField]] = [i[ipDomain]]

            if (i[headerExpiresField] in headerExpires) and (i[ipDomain] not in headerExpires[i[headerExpiresField]]):
                headerExpires[i[headerExpiresField]].append(i[ipDomain])
            elif i[headerExpiresField] not in headerExpires:
                headerExpires[i[headerExpiresField]] = [i[ipDomain]]


            if (i[pragmaField] in pragma) and (i[ipDomain] not in pragma[i[pragmaField]]):
                pragma[i[pragmaField]].append(i[ipDomain])
            elif i[pragmaField] not in pragma:
                pragma[i[pragmaField]] = [i[ipDomain]]

            if (i[locationField] in location) and (i[ipDomain] not in location[i[locationField]]):
                location[i[locationField]].append(i[ipDomain])
            elif i[locationField] not in location:
                location[i[locationField]] = [i[ipDomain]]




if port == 443:
    pKNotPresent = 0
    pkNp =0
    with open('zgrab_parse_'+now+"/public_keys_"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Public Key','Number of Ips/Domains','Ip/Domain list'])
        for i in dictionaryPk:
            if i =='Not Present':
                pKNotPresent = len(dictionaryPk['Not Present'])
                pkNp =1
            writer.writerow([i,len(dictionaryPk[i]),dictionaryPk[i]])
    myfile.close()

    pKLengthNotPresent =0
    pkLNp=0
    with open('zgrab_parse_'+now+"/public_keys_length_"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Public Key Length','Number of Ips/Domains','Ip/Domain list'])
        for i in pKLength:
            if i =='Not Present':
                pKLengthNotPresent =len(pKLength['Not Present'])
                pkLNp=1

            writer.writerow([i,len(pKLength[i]),pKLength[i]])
    myfile.close()

    secureRNotPresent = 0
    sNp=0
    secureR=0
    with open('zgrab_parse_'+now+"/secure_renegotiation_"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Secure renegotiation','Number of Ips/Domains','Ip/Domain list'])
        for i in secureRegotitation:
            if i =='Not Present':
                secureRNotPresent=len(secureRegotitation['Not Present'])
                sNp=1
            elif i =='False':
                secureR = len(secureRegotitation['False'])
            writer.writerow([i,len(secureRegotitation[i]),secureRegotitation[i]])
    myfile.close()

    tlsNotPresent = 0
    tNp=0
    with open('zgrab_parse_'+now+"/tls_"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Tls Version','Number of Ips/Domains','Ip/Domain list'])
        for i in tls:
            if i =='Not Present':
                tlsNotPresent = len(tls['Not Present'])
                tNp =1
            writer.writerow([i,len(tls[i]),tls[i]])
    myfile.close()


    selfSignedNotPresent=0
    seNp=0
    notSelfSigned=0
    isSelfSigned=0
    with open('zgrab_parse_'+now+"/self_signed_"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Self Signed','Number of Ips/Domains','Ip/Domain list'])
        for i in selfSigned:
            if i =='Not Present':
                selfSignedNotPresent = len(selfSigned['Not Present'])
                seNp=1
            elif i == 'False':
                notSelfSigned=len(selfSigned['False'])
            elif i == 'True':
                isSelfSigned=len(selfSigned['True'])
            writer.writerow([i,len(selfSigned[i]),selfSigned[i]])
    myfile.close()

    browserTrustedNotPresent=0
    bNp =0
    notBrowserTrusted =0
    with open('zgrab_parse_'+now+"/browser_trusted_"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Browser Trusted','Number of Ips/Domains','Ip/Domain list'])
        for i in browserTrusted:
            if i =='Not Present':
                browserTrustedNotPresent = len(browserTrusted['Not Present'])
                bNp =1
            elif i =='False':
                    notBrowserTrusted=len(browserTrusted['False'])
            writer.writerow([i,len(browserTrusted[i]),browserTrusted[i]])
    myfile.close()



    cipherSuiteNotPresent=0
    cNp=0
    with open('zgrab_parse_'+now+"/cipher_suite_"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Cipher Suite','Number of Ips/Domains','Ip/Domain list'])
        for i in cipherSuite:
            if i =='Not Present':
                cipherSuiteNotPresent=len(cipherSuite['Not Present'])
                cNp =1
            writer.writerow([i,len(cipherSuite[i]),cipherSuite[i]])
    myfile.close()

    keyAlgorithmNotPresent=0
    kNp =0

    with open('zgrab_parse_'+now+"/key_algorithm_"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Key Algorithm','Number of Ips/Domains','Ip/Domain list'])
        for i in keyAlgorithm:
            if i =='Not Present':
                keyAlgorithmNotPresent = len(keyAlgorithm['Not Present'])
                kNp=1
            writer.writerow([i,len(keyAlgorithm[i]),keyAlgorithm[i]])
    myfile.close()

    signatureAlgorithmNotPresent=0
    sigNp=0
    with open('zgrab_parse_'+now+"/signature_algorithm_"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Signature Algorithm','Number of Ips/Domains','Ip/Domain list'])
        for i in signatureAlgorithm:
            if i =='Not Present':
                signatureAlgorithmNotPresent=len(signatureAlgorithm['Not Present'])
                sigNp =1
            writer.writerow([i,len(signatureAlgorithm[i]),signatureAlgorithm[i]])
    myfile.close()

    curveIdNotPresent=0
    cINp=0
    with open('zgrab_parse_'+now+"/curve_id_"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Curve Id','Number of Ips/Domains','Ip/Domain list'])
        for i in curveId:
            if i =='Not Present':
                curveIdNotPresent=len(curveId['Not Present'])
                cINp =1
            writer.writerow([i,len(curveId[i]),curveId[i]])
    myfile.close()

    compressionMethodNotPresent=0
    cMNp=0
    with open('zgrab_parse_'+now+"/compression_method_"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Compression Method','Number of Ips/Domains','Ip/Domain list'])
        for i in compressionMethod:
            #print(i)
            if i =='Not Present':
                compressionMethodNotPresent=len(compressionMethod['Not Present'])
                cMNp =1
            writer.writerow([i,len(compressionMethod[i]),compressionMethod[i]])
    myfile.close()



statusCodeNotPresent =0
stNp=0
with open('zgrab_parse_'+now+"/status_codes_"+now+".csv", "w") as myfile:
    writer=csv.writer(myfile)
    writer.writerow(['Status Code','Number of Ips/Domains','Ip/Domain list'])
    for i in statusCode:
        if i =='Not Present':
            statusCodeNotPresent = len(statusCode['Not Present'])
            stNp=1
        writer.writerow([i,len(statusCode[i]),statusCode[i]])
myfile.close()

cacheControlNotPresent =0
cCNp=0
with open('zgrab_parse_'+now+"/cache_control_"+now+".csv", "w") as myfile:
    writer=csv.writer(myfile)
    writer.writerow(['cache control','Number of Ips/Domains','Ip/Domain list'])
    for i in cacheControl:
        if i =='Not Present':
            cacheControlNotPresent =len(cacheControl['Not Present'])
            cCNp=1
        writer.writerow([i,len(cacheControl[i]),cacheControl[i]])
myfile.close()

locationNotPresent =0
lNp=0
with open('zgrab_parse_'+now+"/location_"+now+".csv", "w") as myfile:
    writer=csv.writer(myfile)
    writer.writerow(['location','Number of Ips/Domains','Ip/Domain list'])
    for i in location:
        if i =='Not Present':
            locationNotPresent =len(location['Not Present'])
            lNp=1
        writer.writerow([i,len(location[i]),location[i]])
myfile.close()


pragmaNotPresent =0
pNp =0
with open('zgrab_parse_'+now+"/pragma_"+now+".csv", "w") as myfile:
    writer=csv.writer(myfile)
    writer.writerow(['Pragma','Number of Ips/Domains','Ip/Domain list'])
    for i in pragma:
        if i =='Not Present':
            pragmaNotPresent =len(pragma['Not Present'])
            pNp =1
        writer.writerow([i,len(pragma[i]),pragma[i]])
myfile.close()

serverNotPresent =0
srNp=0
with open('zgrab_parse_'+now+"/server_"+now+".csv", "w") as myfile:
    writer=csv.writer(myfile)
    writer.writerow(['Server','Number of Ips/Domains','Ip/Domain list'])
    for i in server:
        if i =='Not Present':
            serverNotPresent =len(server['Not Present'])
            srNp =1
        writer.writerow([i,len(server[i]),server[i]])
myfile.close()




#summary of programme execution
summary_f="summary_parse_"+now+".txt"
summary_fp=open('zgrab_parse_'+now+'/'+summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")" +  " with file " + sys.argv[1]+ " and  Arguments " +  sys.argv[2] +" "+ sys.argv[3]
print >>summary_fp, "Files created:"
print >>summary_fp, str(len(ipsDomains)) + " Unique Ips/Domains"
#port80 relavent fields
print >>summary_fp, str(len(statusCode)-stNp) + " unique status code"
print >>summary_fp, str(statusCodeNotPresent) + " Ips/Domains where status code fields not present"
print >>summary_fp, str(len(server)-srNp) + " unique servers"
print >>summary_fp, str(serverNotPresent) + " Ips/Domains where server field not present"
print >>summary_fp, str(len(pragma)-pNp) + " unique pragma"
print >>summary_fp, str(pragmaNotPresent) + " Ips/Domains where pragma field not present"
print >>summary_fp, str(len(cacheControl)-cCNp) + " unique cache control"
print >>summary_fp, str(cacheControlNotPresent) + " Ips/Domains where cache control field not present"

#port443 relavent fields
if port == 443:
    print >>summary_fp, str(len(dictionaryPk)-pkNp) + " unique public Keys"
    print >>summary_fp, str(pKNotPresent) + " Ips/Domains where public Key fields not present"
    print >>summary_fp, str(len(secureRegotitation['True'])) + " Ip/Domains where secure recognition is true"
    print >>summary_fp, str(secureR) + " Ip/Domains where secure recognition is false"
    print >>summary_fp, str(secureRNotPresent) + " secure recognition field not presented"
    print >>summary_fp, str(len(signatureAlgorithm)-sigNp) + " unique Signature Algorithms"
    print >>summary_fp, str(signatureAlgorithmNotPresent) + " Ips/Domains where Signature Algorithm field Not present"
    print >>summary_fp, str(len(cipherSuite)-cNp) + " unique cipher suites"
    print >>summary_fp, str(cipherSuiteNotPresent) + " Ip/Domains where cipher suite field not present"
    print >>summary_fp, str(notBrowserTrusted) + " Ips/Domains are not Browser Trusted"
    print >>summary_fp, str(len(browserTrusted['True'])) + " Ips/Domains are Browser Trusted"
    print >>summary_fp, str(browserTrustedNotPresent) + " Ips/Domains where Browser Trusted field not present"
    print >>summary_fp, str(len(tls)-tNp) + " unique tls versions found"
    print >>summary_fp, str(tlsNotPresent) + " Ips/Domains where tls field not present"
    print >>summary_fp, str(len(keyAlgorithm)-kNp) + " unique Key Algorithms used"
    print >>summary_fp, str(keyAlgorithmNotPresent) + " Ips/domain where Key Algorithm field not present"
    print >>summary_fp, str(notSelfSigned) + " Ips/Domains do not have self signed certs"
    print >>summary_fp, str(isSelfSigned) + " Ips/Domains have self signed certs"
    print >>summary_fp, str(selfSignedNotPresent) + " Ips/Domains where self signed field not Present"
    print >>summary_fp, str(len(curveId)-cINp) + " unique curve Ids present"
    print >>summary_fp, str(curveIdNotPresent) + " Ips/domain where curve Id field not present"
    print >>summary_fp, str(len(compressionMethod)-cMNp) + " unique Compression Methods present"
    print >>summary_fp, str(compressionMethodNotPresent) + " Ips/domain where Compression Method field not present"
