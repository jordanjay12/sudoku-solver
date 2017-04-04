#!/bin/bash

python3 grid_parser.py easy_puzzles.txt
shopt -s nullglob

index=0
declare -a array
start=$(date +%s%N)
for file in test_file*.txt;
do
	TEST_FILE="${file##*/}"
#	array[index]=$TEST_FILE
	begin=$(date +%s%N)
	python3 sud2sat.py  $TEST_FILE -minisat -extended=false > "input.in"
	minisat "input.in" "output.out" >> logfile.txt
	python3 sat2sud.py "output.out" -minisat >> solution.txt
	end=$(date +%s%N)	
	total_time=$(expr $end - $begin)
	echo "Total time (nanoseconds): $total_time"$'\n' >> solution.txt
#	echo "$TEST_FILE"
	index=$(expr $index + 1)
done |sort -V
finish=$(date +%s%N)
runtime=$(expr $(expr $finish - $start) / 50)
echo "Average run time (nanoseconds): $runtime"$'\n' >> solution.txt
rm -rf test_file*.txt
rm -rf input*.in
rm -rf output*.out
