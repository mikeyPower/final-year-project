#!/bin/bash


#Get time stamp
TIME_STAMP=$(date +%s)
#touch zgrab_domain_p80_$TIME_STAMP.csv
touch summary_wordcloud_$TIME_STAMP.txt

sed 1d $1 > output
while IFS=, read -a b;
do
   IP_ADDR = ${b[2]}
   nb=${#b[@]}
   ${b[$((nb - 1))]} > html_page.txt
   cat html_page.txt | grep -o 'title=.*>' | sed -e 's/title /\ntitle /g' | sed -e 's/title=['"'"'"]//' -e 's/["'"'"'].*$//' -e '/^$/ d' > words.txt
   cat html_page.txt | grep -o "<title>[^<]*" | sed -e 's/<[^>]*>//g' >> words.txt
   cat html_page.txt | grep -o '<a .*href=.*>' | sed -e 's/<a /\n<a /g' | sed -e 's/<a .*href=['"'"'"]//' -e 's/["'"'"'].*$//' -e '/^$/ d' >> words.txt
   
   wordcloud_cli.py --text words.txt --imagefile $IP_ADDR.png
done < output #removing header line

#Summary results
echo 'Ran wordcloud.sh at '$(date -d @$TIME_STAMP +"%d-%m-%Y %T") >> summary_wordcloud_$TIME_STAMP.txt
echo 'Input file: ' >> summary_wordcloud_$TIME_STAMP.txt
echo "$1" >> summary_wordcloud_$TIME_STAMP.txt
echo "Files created:" >> summary_wordcloud_$TIME_STAMP.txt
echo $2 >> summary_wordcloud_$TIME_STAMP.txt

