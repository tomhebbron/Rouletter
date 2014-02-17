
#include "Rouletter.hpp"
#include <random>
#include <iostream>

void doit(int x)
{
	std::uniform_real_distribution<double> unif(0.0,1.0);
	//std::default_random_engine re;
	std::random_device re;

	int eyes[4] = {1,1,1,4};

	Rouletter::Rouletter<int> wheel1(eyes,4);

	int counts[4] = {0,0,0,0};

	for(unsigned int i=0; i<x; ++i)
	{
		int luck = wheel1.spin(unif(re)) ;
		std::cout << luck << ' ';
		counts[luck]++;
	}
	std::cout << std::endl ;

	for(int i=0; i<4; ++i)
	{
	std::cout << '\n' << counts[i] << ' ';
	}


}


#if defined(WIN32) || defined(_WIN32) || defined(__WIN32) && !defined(__CYGWIN__)
#include <tchar.h>
int _tmain(int argc, _TCHAR* argv[])
#else
int main(int argc, char* argv[])
#endif
{
	doit(100);
	std::cout << '\n';
	doit(1000);
	std::cout << '\n';
	doit(1000);
	return 0;
}


