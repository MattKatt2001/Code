#include <iostream>
#include "monster.hpp"

monster::monster(int health)
{
	_health = health;
};

bool monster::isAlive()
{
	return _health > 0;
}

void monster::set_health(int health)
{
	_health = health;
}

int monster::get_health()
{
	return _health;
}

void monster::takeDamage(int x)
{
	_health -= x;
}
