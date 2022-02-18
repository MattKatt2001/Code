#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>
using namespace std;

class race
{
private:
	int _length;
	int _racers;

public:
	race(int length, int racers)
	{
		_length = length;
		_racers = racers;
	}

	void set_length(int length)
	{
		_length = length;
	}

	int get_length()
	{
		return _length;
	}

	void set_racers(int racers)
	{
		_racers = racers;
	}

	int get_racers()
	{
		return _racers;
	}

	void start(human human, runner runner)
	{
		int x = human.get_speed();
		int y = runner.get_speed();

		for (int i = 0; _length > -1; _length -= x)
		{
			i += 1;
			cout<<_length<<"\n";
			if (_length <= 0)
			{
				cout<<"JOe mama";
			}
		}
	}
};
