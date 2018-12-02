#include<stdio.h>
#include <stdlib.h>

int main()
{
	int a;
	float b, X;
	scanf("%d%f", &a, &b);
	X = a / b;
	printf("%0.3f km/l\n", X);
	return 0;
}