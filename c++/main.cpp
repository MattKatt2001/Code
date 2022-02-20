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
	human Matt(20, 90, "Male", "Matthew", 187 ,10);
	runner Usain(35 ,94, "Male", "Usain", 195, 10);

	race cup(100,2);
	cup.start(Matt, Usain);
	return 0;
}
