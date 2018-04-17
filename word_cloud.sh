##!/bin/bash

#Get time stamp
TIME_STAMP=$(date +%s)

#touch summary_wordcloud_$TIME_STAMP.txt
touch summary_wordcloud_$TIME_STAMP.txt
counterNoWords=0
wordsPresent=0
for f in $1*.txt;
do
  #IP_ADDR=echo $f | sed 's/.\{4\}$//'
  IP_ADDR=${f::-4}
  #echo $IP_ADDR
  #cat $f

cat $f | grep -io 'title=.*>' | sed -e 's/title /\ntitle /g' | sed -e 's/title=['"'"'"]//' -e 's/["'"'"'].*$//' -e '/^$/ d' > words.txt
cat $f | grep -io "<title>[^<]*" | sed -e 's/<[^>]*>//g' >> words.txt
cat $f | grep -io '<a .*href=.*>' | sed -e 's/<a /\n<a /g' | sed -e 's/<a .*href=['"'"'"]//' -e 's/["'"'"'].*$//' -e '/^$/ d' >> words.txt

#Check if file is empty
if [ -s words.txt ]
then
   #echo "$f has some data."
   wordcloud_cli.py --text words.txt --imagefile $IP_ADDR.png
   wordsPresent=$((wordsPresent+1))
      # do something as file has data
else
   #echo "words.txt is empty."
   counterNoWords=$((counterNoWords+1))
      # do something as file is empty
fi
done

rm -rf words.txt

#Summary results
echo 'Ran wordcloud.sh at '$(date -d @$TIME_STAMP +"%d-%m-%Y %T") >> summary_wordcloud_$TIME_STAMP.txt
echo 'Input file: ' >> summary_wordcloud_$TIME_STAMP.txt
echo "$1" >> summary_wordcloud_$TIME_STAMP.txt
echo "Files created:" >> summary_wordcloud_$TIME_STAMP.txt
echo $2 >> summary_wordcloud_$TIME_STAMP.txt
echo "Number of Ips with Title and hrefs: $wordsPresent" >> summary_wordcloud_$TIME_STAMP.txt
echo "Number of Ips with Title and hrefs not present: $counterNoWords" >> summary_wordcloud_$TIME_STAMP.txt
