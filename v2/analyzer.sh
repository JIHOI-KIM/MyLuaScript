#!/bin/bash

if [ -z $2 ]; then
	echo "Usage: analyzer.sh [Dir] [OUT NAME]"
	exit 0
fi

rm out.csv
echo '"ENV","Prefix","Number","","Triple","Bug","","Hash","PC","Depth","#0","#1","#2","#3","#4"' > out.csv 

COUNT=0
for file in $1/*.lua; do

	let COUNT++
	echo -n "[$COUNT] Examing file" $file" ..."

	timeout 3s clang64lua $file 2>temp1.log 1>/dev/null
	python3 asan.py $file clang64lua
	
	rm temp1.log

	timeout 3s clang32lua $file 2>temp1.log 1>/dev/null
	python3 asan.py $file clang32lua
	
	rm temp1.log

	timeout 3s gcc64lua $file 2>temp1.log 1>/dev/null
	python3 asan.py $file gcc64lua
	
	rm temp1.log

	timeout 3s gcc32lua $file 2>temp1.log 1>/dev/null
	python3 asan.py $file gcc32lua
	
	rm temp1.log
	
	echo "" >> out.csv
	echo "Done."

done

mv out.csv out_$2.csv
echo "Created File: out_$2.csv"
