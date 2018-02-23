#!/usr/bin/python
import os
import socket
import sys
import csv
import time
import json
from nested_lookup import nested_lookup
from datetime import datetime
from pprint import pprint
from flatten_json import flatten
'''
#!/usr/bin/python3 (running in python 3) Will remove 'u' which is a unicode character

In production might swap over to jq instead, testing both methods?

'''


#the timestamp, in time_t format
now=str(int(time.time()))
str_now=str(datetime.now())



if len(sys.argv)==2:
    file = sys.argv[1]



if not os.path.isfile(file) or not os.access(file,os.R_OK):
    print"Can't read input file: " + file + " - exiting"
    sys.exit(1)

with open(file) as json_file:
    data = json.load(json_file)

'''
for key, value in data.items():
    pprint("Key:")
    pprint(key)
#print(data)

'''

#Print a flatten version of the json file
pprint(flatten(data))
hash_algorithm = nested_lookup('hash_algorithm', data)



with open("json_test_"+now+".csv", "w") as myfile:
    writer=csv.writer(myfile)
    writer.writerow(['hash_algorithm'])
    writer.writerow(hash_algorithm)
myfile.close()




#summary report
summary_f="summary_json_"+now+".txt"
summary_fp=open(summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")" +  " with file " + sys.argv[1]
print >>summary_fp, "Files created:"
print >>summary_fp, "\tjson_test_"+now+".csv"