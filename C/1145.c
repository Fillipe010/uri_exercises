#include<stdio.h>

int main(void){
	int X, Y, i;
	scanf("%d%d", &X, &Y);
	for (i = 1; i <= Y; ++i){
		if (i % X == 0){
			printf("%d\n",i);
		} else {
			printf("%d ", i);
		}
	}
	return 0;
}