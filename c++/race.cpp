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
		if(h>r)
		{
			cout << human.get_name() + " wins!";
		}
		else
		{
			cout << runner.get_name() + " wins!";
		}
	}

	void start(human human)//overloaded method do for runner as well
	{
		int x = human.get_speed();
		int h = compare(_length, x);
	}

	int compare(int length, int speed)
	{
		int result = length * speed;
		return result;
	}
};
