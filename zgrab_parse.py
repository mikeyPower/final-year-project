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

#create directory for outputted results
try:
    os.makedirs('zgrab_parse_'+now)
except OSError:
    if not os.path.isdir(path):
        raise

if sys.argv[2] == 'domain':
    ipDomain = 0
else:
    ipDomain =1

if sys.argv[3] == '443':
    port = 443
else:
    port =80

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
server ={}
cacheControl={}
headerExpires={}
pragma={}
location={}

with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    readCSV.next() #Skip first line (Header line)

    for i in readCSV:

        if i[ipDomain] not in ipsDomains:


            #Get Public Keys

            ipsDomains.append(i[ipDomain])
            if port == 443:

                if (i[21] in dictionaryPk) and (i[ipDomain] not in dictionaryPk[i[21]]):
                    dictionaryPk[i[21]].append(i[ipDomain])
                elif i[21] not in dictionaryPk:
                    dictionaryPk[i[21]] = [i[ipDomain]]


                if (i[9] in secureRegotitation) and (i[ipDomain] not in secureRegotitation[i[9]]):
                    secureRegotitation[i[9]].append(i[ipDomain])
                elif i[9] not in secureRegotitation:
                    secureRegotitation[i[9]] = [i[ipDomain]]


                if (i[10] in tls) and (i[ipDomain] not in tls[i[10]]):
                    tls[i[10]].append(i[ipDomain])
                elif i[10] not in tls:
                    tls[i[10]] = [i[ipDomain]]

                if (i[11] in selfSigned) and (i[ipDomain] not in selfSigned[i[11]]):
                    selfSigned[i[11]].append(i[ipDomain])
                elif i[11] not in selfSigned:
                    selfSigned[i[11]] = [i[ipDomain]]



                if (i[14] in browserTrusted) and (i[ipDomain] not in browserTrusted[i[14]]):
                    browserTrusted[i[14]].append(i[ipDomain])
                elif i[14] not in browserTrusted:
                    browserTrusted[i[14]] = [i[ipDomain]]


                if (i[15] in cipherSuite) and (i[ipDomain] not in cipherSuite[i[15]]):
                    cipherSuite[i[15]].append(i[ipDomain])
                elif i[15] not in cipherSuite:
                    cipherSuite[i[15]] = [i[ipDomain]]

                if (i[-1] in curveId) and (i[ipDomain] not in curveId[i[-1]]):
                    curveId[i[-1]].append(i[ipDomain])
                elif i[-1] not in curveId:
                    curveId[i[-1]] = [i[ipDomain]]


                if (i[-2] in keyAlgorithm) and (i[ipDomain] not in keyAlgorithm[i[-2]]):
                    keyAlgorithm[i[-2]].append(i[ipDomain])
                elif i[-2] not in keyAlgorithm:
                    keyAlgorithm[i[-2]] = [i[ipDomain]]


                if (i[-3] in signatureAlgorithm) and (i[ipDomain] not in signatureAlgorithm[i[-3]]):
                    signatureAlgorithm[i[-3]].append(i[ipDomain])
                elif i[-4] not in signatureAlgorithm:
                    signatureAlgorithm[i[-3]] = [i[ipDomain]]

                if (i[-4] in pKLength) and (i[ipDomain] not in pKLength[i[-4]]):
                    pKLength[i[-4]].append(i[ipDomain])
                elif i[-4] not in pKLength:
                    pKLength[i[-4]] = [i[ipDomain]]



            if (i[3] in server) and (i[ipDomain] not in server[i[3]]):
                server[i[3]].append(i[ipDomain])
            elif i[3] not in server:
                server[i[3]] = [i[ipDomain]]


            if (i[4] in statusCode) and (i[ipDomain] not in statusCode[i[4]]):
                statusCode[i[4]].append(i[ipDomain])
            elif i[4] not in statusCode:
                statusCode[i[4]] = [i[ipDomain]]



            if (i[5] in cacheControl) and (i[ipDomain] not in cacheControl[i[5]]):
                cacheControl[i[5]].append(i[ipDomain])
            elif i[5] not in cacheControl:
                cacheControl[i[5]] = [i[ipDomain]]

            if (i[6] in headerExpires) and (i[ipDomain] not in headerExpires[i[6]]):
                headerExpires[i[6]].append(i[ipDomain])
            elif i[6] not in headerExpires:
                headerExpires[i[6]] = [i[ipDomain]]


            if (i[7] in pragma) and (i[ipDomain] not in pragma[i[7]]):
                pragma[i[7]].append(i[ipDomain])
            elif i[7] not in pragma:
                pragma[i[7]] = [i[ipDomain]]

            if (i[8] in location) and (i[ipDomain] not in location[i[8]]):
                location[i[8]].append(i[ipDomain])
            elif i[8] not in location:
                location[i[8]] = [i[ipDomain]]




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
    with open('zgrab_parse_'+now+"/secure_recognition_"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Secure recognition','Number of Ips/Domains','Ip/Domain list'])
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

#summary of programme execution
summary_f="summary_parse_"+now+".txt"
summary_fp=open('zgrab_parse_'+now+'/'+summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")" +  " with file " + sys.argv[1]+ " and  Arguments " +  sys.argv[2] +" "+ sys.argv[3]
print >>summary_fp, "Files created:"
print >>summary_fp, str(len(ipsDomains)) + " Unique Ips/Domains"
#port80
print >>summary_fp, str(len(statusCode)-stNp) + " unique status code"
print >>summary_fp, str(statusCodeNotPresent) + " Ips/Domains where status code fields not present"

#port443
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
