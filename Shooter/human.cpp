#include <iostream>
#include "human.hpp"

	human::human(std::string name, int health, int speed, int strength)
	{
		_name = name;
		_health = health;
		_speed = speed;
		_strength = strength;
	};

	void human::set_name(std::string name)
	{
		_name = name;
	}

	std::string human::get_name()
	{
		return _name;
	}

	void human::set_health(int health)
	{
		_health = health;
	}

	int human::get_health()
	{
		return _health;
	}

	void human::set_speed(int speed)
	{
		_speed = speed;
	}

	int human::get_speed()
	{
		return _speed;
	}

	void human::set_strength(int strength)
	{
		_strength = strength;
	}

	int human::get_strength()
	{
		return _strength;
	}

	void human::takeDamage(int x)
	{
		_health -= x;
	}
