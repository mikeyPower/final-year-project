#!/usr/bin/python
import csv
import sys
from functions import dateRange
from datetime import datetime
import time

#Get timestamp of programme execution
now=str(int(time.time()))
str_now=str(datetime.now())
csvFile = sys.argv[1]

if sys.argv[2] == 'domain':
    ipDomain = 0
else:
    ipDomain =1

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

with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    readCSV.next() #Skip first line (Header line)

    for i in readCSV:
        #print(ipDomain,'HI')
        if i[ipDomain] not in ipsDomains:
            #print(i[ipDomain],'NO')

            #Get Public Keys
            ipsDomains.append(i[ipDomain])
            if (i[21] in dictionaryPk) and (i[ipDomain] not in dictionaryPk[i[21]]):
                dictionaryPk[i[21]].append(i[ipDomain])
            elif i[21] not in dictionaryPk:
                dictionaryPk[i[21]] = [i[ipDomain]]

            #Get Status Code
            if (i[4] in statusCode) and (i[ipDomain] not in statusCode[i[4]]):
                statusCode[i[4]].append(i[ipDomain])
            elif i[4] not in statusCode:
                statusCode[i[4]] = [i[ipDomain]]

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




            if (i[-1] in keyAlgorithm) and (i[ipDomain] not in keyAlgorithm[i[-1]]):
                keyAlgorithm[i[-1]].append(i[ipDomain])
            elif i[-1] not in keyAlgorithm:
                keyAlgorithm[i[-1]] = [i[ipDomain]]


            if (i[-2] in signatureAlgorithm) and (i[ipDomain] not in signatureAlgorithm[i[-2]]):
                signatureAlgorithm[i[-2]].append(i[ipDomain])
            elif i[-2] not in signatureAlgorithm:
                signatureAlgorithm[i[-2]] = [i[ipDomain]]

            if (i[-3] in pKLength) and (i[ipDomain] not in pKLength[i[-3]]):
                pKLength[i[-3]].append(i[ipDomain])
            elif i[-3] not in pKLength:
                pKLength[i[-3]] = [i[ipDomain]]


try:
    secureR=len(secureRegotitation['False'])
except:
    secureR = 0


try:
    secureRNotPresent=len(secureRegotitation['Not Present'])
    sNp=1
except:
    secureRNotPresent = 0
    sNp=0


try:
    pKNotPresent = len(dictionaryPk['Not Present'])
    pkNp =1
except:
    pKNotPresent = 0
    pkNp =0

try:
    browserTrustedNotPresent = len(browserTrusted['Not Present'])
    bNp =1
except:
    browserTrustedNotPresent=0
    bNp =0

try:
    signatureAlgorithmNotPresent=len(signatureAlgorithm['Not Present'])
    sigNp =1
except:
    signatureAlgorithmNotPresent=0
    sigNp=0

try:
    cipherSuiteNotPresent=len(cipherSuite['Not Present'])
    cNp =1
except:
    cipherSuiteNotPresent=0
    cNp=0

try:
    tlsNotPresent = len(tlsNotPresent['Not Present'])
    tNp =1
except:
    tlsNotPresent = 0
    tNp=0


try:
    keyAlgorithmNotPresent = len(keyAlgorithm['Not Present'])
    kNp=1
except:
    keyAlgorithmNotPresent=0
    kNp =0

try:
    selfSignedNotPresent = len(selfSigned['Not Present'])
    seNp=1
except:
    selfSignedNotPresent=0
    seNp=0


print(browserTrusted)

#summary of programme execution
summary_f="summary_parse_"+now+".txt"
summary_fp=open(summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")" +  " with file " + sys.argv[1]
print >>summary_fp, "Files created:"
print >>summary_fp, str(len(ipsDomains)) + " Unique Ips/Domains"
print >>summary_fp, str(len(dictionaryPk)-pkNp) + " different public Keys"
print >>summary_fp, str(pKNotPresent) + " public Key fields not present"
print >>summary_fp, str(len(secureRegotitation['True'])) + " Number of secure recognition that are true"
print >>summary_fp, str(secureR) + " Number of secure recognition that are false"
print >>summary_fp, str(secureRNotPresent) + " secure recognition field not presented"
print >>summary_fp, str(len(signatureAlgorithm)-sigNp) + " different Signature Algorithms"
print >>summary_fp, str(signatureAlgorithmNotPresent) + " Signature Algorithm field Not present"
print >>summary_fp, str(len(cipherSuite)-cNp) + " different cipher suites"
print >>summary_fp, str(cipherSuiteNotPresent) + " cipher suites field not present"
print >>summary_fp, str(len(browserTrusted['False'])) + " are not Browser Trusted"
print >>summary_fp, str(len(browserTrusted['True'])) + " are Browser Trusted"
print >>summary_fp, str(browserTrustedNotPresent) + " Browser Trusted field not present"
print >>summary_fp, str(len(tls)-tNp) + " different tls versions found"
print >>summary_fp, str(len(keyAlgorithm)-kNp) + " Key Algorithms used"
print >>summary_fp, str(keyAlgorithmNotPresent) + " Key Algorithm field not present"
print >>summary_fp, str(len(selfSigned['False'])) + " are not self signed certs"
print >>summary_fp, str(len(selfSigned['True'])) + " are self signed certs"
print >>summary_fp, str(selfSignedNotPresent) + " self signed field not Present"
