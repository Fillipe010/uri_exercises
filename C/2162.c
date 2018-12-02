#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *vet, n, i, cndtn = 1;
    
    /* LE O TAMANHO DO VETOR */
    scanf("%d", &n);

    /* ALOCA MEMORIA PARA O VETOR DE INTEIROS */
    vet = (int *) malloc(n * sizeof(int));

    /* PREENCHE O VETOR */
    for(i=0; i<n; i++){
        scanf("%d", &vet[i]);
    }

    /* VERIFICACOES */
    if(n==2 && vet[0]==vet[1]) cndtn = 0;
    else
    {
        for(i=2; i<n; i++)
        {
            if(vet[i] >= vet[i-1] && vet[i-1] >= vet[i-2])
            {
                cndtn = 0;
                break;
            }
            else if(vet[i] <= vet[i-1] && vet[i-1] <= vet[i-2])
            {
                cndtn = 0;
                break;
            }
        }
    }

    /* IMPRESSAO DOS RESULTADOS */
    printf((cndtn==1)?"1\n":"0\n");
    return 0;
}