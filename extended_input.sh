#!/bin/bash

python3 extended_parser.py hard_puzzles.txt
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
	minisat "input.in" "output.out" >> extended_logfile.txt
	python3 sat2sud.py "output.out" -minisat >> extended_solution.txt
	end=$(date +%s%N)	
	total_time=$(expr $end - $begin)
	echo "Total time (nanoseconds): $total_time"$'\n' >> extended_solution.txt
#	echo "$TEST_FILE"
	index=$(expr $index + 1)
done |sort -V
finish=$(date +%s%N)
runtime=$(expr $(expr $finish - $start) / 95)
echo "Average run time (nanoseconds): $runtime"$'\n' >> extended_solution.txt
rm -rf test_file*.txt
rm -rf input*.in
rm -rf output*.out
