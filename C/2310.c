#include <stdio.h>

int main(){
	int N, i;
	double St, Bt, At, S, B, A, S1, B1, A1, aux;
	char nome[10];

	scanf("%d", &N);

	S = B = A = S1 = B1 = A1 = 0;
	St = Bt = At = 0.0;

	for (i = 0; i < N; i++){
		scanf("%s", &nome);
		scanf("%lf", &aux);
		S = S + aux;
		scanf("%lf", &aux);
		B = B + aux;
		scanf("%lf", &aux);
		A = A + aux;
		scanf("%lf", &aux);
		S1 = S1 + aux;
		scanf("%lf", &aux);
		B1 = B1 + aux;
		scanf("%lf", &aux);
		A1 = A1 + aux;
	}

	St = ((S1 / S) * 100);
	Bt = ((B1 / B) * 100);
	At = ((A1 / A) * 100);

	printf("Pontos de Saque: %0.2lf %%.\n", St);
	printf("Pontos de Bloqueio: %0.2lf %%.\n", Bt);
	printf("Pontos de Ataque: %0.2lf %%.\n", At);

}