#include<stdio.h>

int main(void){
	float vet[6], x, media;
	int i, count;
	for (i = 0; i < 6; ++i){
		scanf("%f", &x);
		vet[i] = x;
	}

	count = 0;
	media = 0;

	for (i = 0; i < 6; ++i){
		if(vet[i] > 0){
			++count;
			media = media + vet[i];
		}
	}

	media = media / count;

	printf("%d valores positivos\n", count);
	printf("%0.1f\n", media);
	
}