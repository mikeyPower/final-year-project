import csv
#Need to define 4 parameter
#Parameters: x = starting time hour


with open('tmp.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    mostCount =0
    mostDate =''

    ports = []
#create a list of times substring till the hour of the csv file
    for t in readCSV:
        ports.append(t[6])
        #print(t[6])

    ports = list(set(ports))


    print(len(ports))

    #store each ip in a multi dimensial array so all ips listenning on port 80 are located at stableIps[0] etc
    stableIps = []
    count =0
    for t in ports:
        stableIps.append([])
        with open('tmp.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for u in readCSV:
                if u[6]==t:
                    stableIps[count].append(u[0]) #could possible place the items as tuples if the nesting of arrays becomes a problem but unsure can i check for intersection and so what with tuples
                else:
	               #break
                    continue
            count = count +1


#find ips that are listenning on both ports
    intersectSet =stableIps[0]
    print(len(intersectSet))
    for i in stableIps[1:]:
         intersectSet = list(set(i).difference(intersectSet))
    print(len(intersectSet))
