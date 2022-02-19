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
		int h = compare(_length, x);
		int r = compare(_length, y);
		cout<<h<<"\n";
		cout<<r<< "\n";
	}

	int compare(int length, int speed)
	{
		int out[1];
		for (int i = 0; length > -1; length -= speed)
		{
			i += 1;
			//cout<<length<<"\n";
			if (length <= 0)
			{
				out[0] = i;
			}
		}
		return out[0];
	}
};
