#include <iostream>
#include "human.cpp"
#include "monster.cpp"

int main()
{
	human Matt("Matthew", 100, 10, 10);
	int mDamage = Matt.get_strength();

	monster monster1(100);

	while(monster1.isAlive())
	{
		monster1.takeDamage(mDamage);
		std::cout<<monster1.get_health()<<"\n";
	}
}
