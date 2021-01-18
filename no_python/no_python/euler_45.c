#include <stdio.h>
void main() {
	int n = 165;
	while (1)
	{
		n++;
		unsigned long long p = n * (3 * n - 1) / 2;
		for (int i = 143; i < n; i++) {
			unsigned long long h = i * (2 * n - 1);
			if (h == p) { 
				printf(h);
				break;
			
			}
		}



	}

}