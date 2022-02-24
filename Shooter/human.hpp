#ifndef HUMAN_H
#define HUMAN_H

class human
{
private:

protected:
	std::string _name;
	int _health;
	int _speed;
	int _strength;

public:
	human(std::string name, int health, int speed, int strength);
	void set_name(std::string name);
	std::string get_name();
	void set_health(int health);
	int get_health();
	void set_speed(int speed);
	int get_speed();
	void set_strength(int strength);
	int get_strength();
	void takeDamage(int x);
};

#endif
