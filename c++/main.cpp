#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>
#include "human.cpp"
#include "race.cpp"
using namespace std;

int main()
{
	human Matt(20, 90, "Male", "Matthew", 187 ,50);
	runner Usain(35 ,94, "Male", "Usain", 195, 10);
	race cup(100,2);//This doesn't actually mean anything atm just creates the object
	cup.start(Matt, Usain);
	return 0;
}
