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
	int last = 0;
	int next = 0;
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
			first = false;
		}
		else
		{
			if (next > last)
				total++;
		}
		last = next;

		
	}

	cout << total << '\n';
	return 0;
}
