#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>
using namespace std;

class human
{
protected:
	int _age;
	int _weight;
	string _gender;
	string _name;
	int _height;
	int _speed;

public:
	human(int age, int weight, string gender, string name, int height, int speed)
	{
		_age = age;
		_weight = weight;
		_gender = gender;
		_name = name;
		_height = height;
		_speed = speed;
	};

	void set_age(int age)
	{
		_age = age;
	}

	int get_age()
	{
		return _age;
	}

	void set_weight(int weight)
	{
		_weight = weight;
	}

	int get_weight()
	{
		return _weight;
	}

	void set_gender(string gender)
	{
		_gender = gender;
	}

	string get_gender()
	{
		return _gender;
	}

	void set_name(string name)
	{
		_name = name;
	}

	string get_name()
	{
		return _name;
	}

	void set_height(int height)
	{
		_height = height;
	}

	int get_height()
	{
		return _height;
	}

	void set_speed(int speed)
	{
		_speed = speed;
	}

	int get_speed()
	{
		return _speed;
	}

	void eat()
	{
		_weight = ++_weight;
	}

	void run()
	{
		_weight = --_weight;
	}
};

class runner: public human
{
public:
	runner(int age, int weight, string gender, string name, int height, int speed): human(age, weight, gender, name, height, speed)
	{
		_age = age;
		_weight = weight;
		_gender = gender;
		_name = name;
		_height = height;
		_speed = speed*1.5;//I know this doesn't exactly make sense given that base human also has speed, think of it as that a runner has better technique and so he gets more out of his base speed
	}

	void sprint()
	{
		_weight = _weight-5;
	}
};
