#include <stdio.h>
#include <stdlib.h>

int main(){

	int *vet, N, i, fall;

	fall = 0;

	/* LE O TAMANHO DO VETOR */
    scanf("%d", &N);

    /* ALOCA MEMORIA PARA O VETOR DE INTEIROS */
    vet = (int *) malloc(N * sizeof(int));

    /* PREENCHE O VETOR */
    for(i = 0; i < N; i++){
        scanf("%d", &vet[i]);
    }

    /* VERIFICACOES */
    for (i = 0; i < N; i++){
    	if (i >= 1){
    		if (vet[i] < vet[i-1]){
    			fall = i + 1;
    			break;
    		}
    	}
    }

    /* IMPRESSAO DO RESULTADO */
    if (fall == 0){
    	printf("0\n");
    } else {
    	printf("%d\n", fall);
    }

    return 0;
}