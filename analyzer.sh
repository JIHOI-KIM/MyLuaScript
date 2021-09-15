#!/bin/bash

if [ -z $1 ]; then
	echo "Usage: analyzer.sh [Dir]"
	exit 0
fi

rm out.csv
echo '"Prefix","Number","-","Triple","Bug","Mini","-","#0","#1","#2","Depth"' > out.csv 

COUNT=0
for file in $1/*.lua; do
	

	let COUNT++
	echo -n "[$COUNT] Examing file" $file" ..."

	lua $file 2>temp1.log 1>/dev/null
	lua $file 2>temp2.log 1>/dev/null
	lua $file 2>temp3.log 1>/dev/null
	
	python3 asan.py $file
	
	rm temp1.log
	rm temp2.log
	rm temp3.log

	echo "Done."

done

echo "Created File: out.csv"
