/*
 *
 * 
 */

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	string fname = "../input.txt";
	int last[3] = {0,0,0};
	int lastTot = 0;
	int idx = 0;
	int next = 0;
	int nextTot = 0;
	int total = 0;
	
	bool first = true;

	ifstream input;
       
	input.open(fname);
	string temp = "";

	while(getline(input, temp))
	{
		next =  atoi(temp.c_str());
		if (first)
		{
			if(idx == 2)
				first = false;
		}
		else
		{
			nextTot = 0;
		
			for (int i = 0; i < 3; i++)
				nextTot += last[i];


			if (nextTot > lastTot)
				total++;
			lastTot = nextTot;
		}
		last[idx] = next;

		idx = (idx + 1) % 3;


		
	}

	cout << total << '\n';
	return 0;
}
