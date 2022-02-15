#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include "human.cpp"
//#include "race.cpp"
using namespace std;

int main()
{
	human Matt(20, 90, "Male", "Matthew", 187 ,10);
	runner Usain(35 ,94, "Male", "Usain", 195, 10);
	cout<<Matt.get_speed()<<"\n";
	cout<<Usain.get_speed()<<"\n";
	return 0;
}

/*int _age;
int _weight;
string _gender;
string _name;
int _height;
int _speed*/
