

input: ../input.txt

../input.txt :
	cd ../.. && ./getInputs.sh 

partA: bin/a.out

bin/a.out: a.cpp
	g++ a.cpp -o bin/a.out


partB: bin/b.out

bin/b.out: b.cpp
	g++ b.cpp -o bin/b.out
