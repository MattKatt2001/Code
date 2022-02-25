#ifndef MONSTER_H
#define MONSTER_H

class monster: public entity
{
private:

protected:

public:
	monster(std::string name, int health, int speed, int strength);
	/*bool isAlive();
	void set_health(int health);
	int get_health();
	void takeDamage(int x);*/
};

#endif
