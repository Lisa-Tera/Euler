#include <iostream>
using namespace std;
int main() {
	
	__int64 t = 1000000000000;
	__int64 t2 =600000000000;
	for (t2= 756872327472; t2<t ; t2++) {
		float r = float(t * (t - 1)) /  float(t2 * (t2 - 1));
		if (r == 2.0) {
			cout <<t <<"\t"<< t2<<endl;
		}

		}
	}
