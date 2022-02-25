#include <iostream>
#include "monster.hpp"

monster::monster(std::string name, int health, int speed, int strength): entity(name, health, speed, strength)
{
	_health = health;
};

/*bool monster::isAlive()
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
}*/
