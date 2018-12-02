#include<stdio.h>

int main(void){
	int i, x, j, numero;
	scanf("%d", &x);

	numero = 1;

	for (i = 1; i <= x; ++i){
		for (j = 0; j < 4; ++j){
			if (numero % 4 == 0){
				printf("PUM\n");
			} else {
				printf("%d ", numero);
			}
			numero = numero + 1;
		}	
	}
	return 0;
}