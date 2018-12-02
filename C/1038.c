#include<stdio.h>

int main(){
	int cod, qnt;
	float vlrTotal;
	scanf("%d%d", &cod, &qnt);

	if (cod == 1)
	{
		vlrTotal = qnt * 4;
	}

	if (cod == 2)
	{
		vlrTotal = qnt * 4.5;
	}

	if (cod == 3)
	{
		vlrTotal = qnt * 5;
	}

	if (cod == 4)
	{
		vlrTotal = qnt * 2;
	}

	if (cod == 5)
	{
		vlrTotal = qnt * 1.5;
	}

	printf("Total: R$ %0.2f\n", vlrTotal);
}