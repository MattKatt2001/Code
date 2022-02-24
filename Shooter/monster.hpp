#ifndef MONSTER_H
#define MONSTER_H

class monster
{
private:

protected:
	int _health;

public:
	monster(int health);
	bool isAlive();
	void set_health(int health);
	int get_health();
	void takeDamage(int x);
};

#endif
