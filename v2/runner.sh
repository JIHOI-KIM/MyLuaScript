#!/bin/bash

for ((i=0;i<=$1;i++))
do
   ./analyzer.sh "DIR"$i $i
done

