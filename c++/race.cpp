#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
//#include "human.cpp"
using namespace std;

class race
{
private:
	int _length;
	human _human();
	runner _runner();

public:
	race(int length, human human(), runner runner())
	{
		_length = length;
		_human = human;
		_runner = runner;
	}

	string commence_race(race race)
	{
		return "joe";
	}
};
