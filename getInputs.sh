#!/bin/bash

aoc="https://adventofcode.com/2021/day"

if [ ! -f "session" ]; then
	echo "Missing session cookie"
	read sesh
	echo "session=$sesh" > session

fi

for d in day*; do
	if [ ! -f "$d/input.txt" ]; then
		#echo $d
		daynum=${d: -2}
		#echo $daynum
		daynum=$(echo $daynum | sed 's/^0*//')
		#echo $daynum

		echo "Grabbing day $daynum."
		curl --cookie "$(cat session)" $aoc/$daynum/input > $d/input.txt

	fi
done
