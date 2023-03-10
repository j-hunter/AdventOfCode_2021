#!/bin/bash

TRUTHS=$( awk -F, ' { print $1 } ' truths.txt )

for i in $TRUTHS ;
do
	echo $i
	mode=$( grep $i truths.txt | awk -F, ' { print $2 } ' )
	echo $mode

	case $mode in
		'py')
			echo "Run py!"
			./runPy.sh $i a
			./runPy.sh $i b
			cp $i/py/*.ans $i/
	esac
done
