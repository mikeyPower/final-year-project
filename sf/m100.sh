#!/bin/bash

#set -x

# make a 100 record test file with synthetic data

# records should look like zmap output with "--output-fields=*", with these fields: 
# saddr,saddr-raw,daddr,daddr-raw,ipid,ttl,sport,dport,seqnum,acknum,window,classification,success,repeat,cooldown,timestamp-str,timestamp-ts,timestamp-us

# copied from one of the options at:
# https://stackoverflow.com/questions/10768160/ip-address-converter
ip2dec()
{ 
	# Convert an IPv4 IP number to its decimal equivalent.
	declare -i a b c d;
	IFS=. read a b c d <<<"$1";
	echo "$(((a<<24)+(b<<16)+(c<<8)+d))";
}

# function to decide if an IP is listening on 80 and/or 443
listeners()
{
	# random for now: 0=>just 80; 1=>just 443; 2=>both
	echo $(( RANDOM % 3 ))
}

# output file will have this many lines:-) 
OFILE=254recs.csv
# don't entirely crap on an old one, give us 1 chance to fix
if [ -f $OFILE ]
then
	cp $OFILE $OFILE.bup
fi

# documentation addrs as per RFC 5737
slash24="192.0.2"
scanner="192.0.2.1"
decscanner=$(ip2dec "$scanner")
# we'll use 20 pretend hosts
bottom=20
top=40
# measurement times
times="\
	2018-02-05T19:00:12.386+0000 \
	2018-02-05T20:00:12.386+0000 \
	2018-02-05T21:00:12.386+0000 \
	2018-02-05T22:00:12.386+0000 \
	2018-02-05T23:00:12.386+0000 \
"

for scantime in $times
do
	for ((hnum=$bottom;hnum<=$top;hnum++))
	do
		ip=$slash24"."$hnum
		decip=$(ip2dec "$ip")
		#echo "$scantime,$ip,$decip,$scanner,$decscanner"
		ports=$(listeners)
		if [[ "$ports" == "0" ]]
		then
			# just 80
			echo "$ip,$decip,$scanner,$decscanner,10219,125,80,39178,4266143625,714081742,8192,synack,1,0,1,$scantime,1517871612,386503" >>$OFILE
		elif [[ "$ports" == "1" ]]
		then
			# just 443
			echo "$ip,$decip,$scanner,$decscanner,10219,125,443,39178,4266143625,714081742,8192,synack,1,0,1,$scantime,1517871612,386503" >>$OFILE
		elif [[ "$ports" == "2" ]]
		then
			# both 
			echo "$ip,$decip,$scanner,$decscanner,10219,125,80,39178,4266143625,714081742,8192,synack,1,0,1,$scantime,1517871612,386503" >>$OFILE
			echo "$ip,$decip,$scanner,$decscanner,10219,125,443,39178,4266143625,714081742,8192,synack,1,0,1,$scantime,1517871612,386503" >>$OFILE
		else
			echo "oops - something odd - exiting at $scantime, $hnum, $ports"
			exit 1
		fi

	done
done


