#include<stdio.h>

int main(void){
	double n, raio, area;
	n = 3.14159;
	scanf("%lf", &raio);
	area = (raio * raio) * n;
	printf("A=%0.4lf\n", area);
	return 0;
}