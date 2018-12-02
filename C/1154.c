#include <stdio.h>

int main(){
	int x, y, count;
	double media, soma;
	count = 0;
	soma = 0;
	x = 1;

	while(x == 1){
		scanf("%d", &y);
		if (y > 0){
			soma = soma + y;
			++count;
		} else {
			x = 0;
		}
	}

	media = soma / count;

	printf("%0.2lf\n", media);

	return 0;
}