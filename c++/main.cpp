#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include "human.cpp"
using namespace std;

int main()
{
	human Matt(20,90,"Male","Matthew",187);
	cout<<Matt.get_weight();
	return 0;
}

/*int _age;
int _weight;
string _gender;
string _name;
int _height;*/
