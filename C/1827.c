#include <stdio.h>
#include <stdlib.h>

int roundNo(float num) { 
    return num < 0 ? num - 0.5 : num + 0.5; 
}

int main(){
	int tamMat, i, j, mat[102][102];
	float aux, m;

	while(scanf("%d", &tamMat)!=EOF){
		/** scanf("%d", &tamMat); **/
		
		if (!tamMat) break;

		aux = tamMat / 3;
		m = tamMat - aux;

		/** INSERE OS VALORES 2, 3 E 4 NA MATRIZ **/
		for (i = 0; i < tamMat; ++i){
			for (j = 0; j < tamMat; ++j){

				if ((i == j) && ((i + j) == (tamMat - 1))){ mat[i][j] = 4; } else {
					if ((i + j) == (tamMat - 1)){mat[i][j] = 3; } else {
						if (i == j){ mat[i][j] = 2; } else {mat[i][j] = 0; }
					}
				}
			}
		}


		/** FAZ O QUADRO DE 1 AO REDOR DO 4 **/

		for(i = aux;i < m;i++){
            for(j = aux;j < m;j++){
                if(i==tamMat/2 && j==tamMat/2) {mat[i][j]=4;}
                else{ mat[i][j]=1; }
            }
        }

		/** IMPRIME A MATRIZ **/
		for(i = 0;i < tamMat;i++){
            for(j = 0;j < tamMat;j++){
                printf("%d", mat[i][j]);
            }
            printf("\n");
        }
        printf("\n");

    }

	return 0;
}
	