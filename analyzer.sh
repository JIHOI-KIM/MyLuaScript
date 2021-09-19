#!/bin/bash

if [ -z $1 ]; then
	echo "Usage: analyzer.sh [Dir]"
	exit 0
fi

rm out.csv
echo '"ENV","Prefix","Number","","Triple","Bug","","Depth","#0","#1","#2"' > out.csv 

COUNT=0
for file in $1/*.lua; do

	let COUNT++
	echo -n "[$COUNT] Examing file" $file" ..."

	timeout 5s clang64lua $file 2>temp1.log 1>/dev/null
	timeout 5s clang64lua $file 2>temp2.log 1>/dev/null
	timeout 5s clang64lua $file 2>temp3.log 1>/dev/null
	python3 asan.py $file clang64lua
	
	rm temp1.log
	rm temp2.log
	rm temp3.log

	timeout 5s clang32lua $file 2>temp1.log 1>/dev/null
	timeout 5s clang32lua $file 2>temp2.log 1>/dev/null
	timeout 5s clang32lua $file 2>temp3.log 1>/dev/null
	python3 asan.py $file clang32lua
	
	rm temp1.log
	rm temp2.log
	rm temp3.log

	timeout 5s gcc64lua $file 2>temp1.log 1>/dev/null
	timeout 5s gcc64lua $file 2>temp2.log 1>/dev/null
	timeout 5s gcc64lua $file 2>temp3.log 1>/dev/null
	python3 asan.py $file gcc64lua
	
	rm temp1.log
	rm temp2.log
	rm temp3.log

	timeout 5s gcc32lua $file 2>temp1.log 1>/dev/null
	timeout 5s gcc32lua $file 2>temp2.log 1>/dev/null
	timeout 5s gcc32lua $file 2>temp3.log 1>/dev/null
	python3 asan.py $file gcc32lua
	
	rm temp1.log
	rm temp2.log
	rm temp3.log
	
	echo "" >> out.csv
	echo "Done."

done

mv out.csv out_$1.csv
echo "Created File: out_$1.csv"
