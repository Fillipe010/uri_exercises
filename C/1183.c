#include <stdio.h>

int main(){
	char O[2];
	double mat[12][12], resultado, aux;
	int i, j;

	resultado = 0;

	scanf("%s", &O);

	for (i = 0; i < 12; ++i){
		for (j = 0; j < 12; ++j){
			scanf("%lf", &mat[i][j]);
		}
	}

	if (O[0] == 'S'){
		for (i = 0; i < 12; ++i){
			for (j = 0; j < 12; ++j){
				if (j > i){
					resultado = resultado + mat[i][j];
				}
			}
		}
		printf("%0.1f\n", resultado);	
	}
	
	if (O[0] == 'M'){
		for (i = 0; i < 12; ++i){
			for (j = 0; j < 12; ++j){
				if (j > i){
					aux = aux + mat[i][j];
					resultado = aux / 66;
				}
			}
		}
		printf("%0.1f\n", resultado);
	}
	return 0;
}