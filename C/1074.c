#include <stdio.h>

int main(){
	int x, y, i, z;
	scanf("%d", &x);

	for (i = 0; i < x; ++i){
		scanf("%d", &y);

		z = 0;

		if (y > 0){
			z = 1;
		} else {
			z  =0;
		}

		if (y == 0){
			printf("NULL\n");
		} else {
			if (y % 2 == 0 && z == 1){
				printf("EVEN POSITIVE\n");
			}

			if (y % 2 == 0 && z == 0){
				printf("EVEN NEGATIVE\n");
			}

			if (y % 2 != 0 && z == 1){
				printf("ODD POSITIVE\n");
			}

			if (y % 2 != 0 && z == 0){
				printf("ODD NEGATIVE\n");
			}
		}
	}
	return 0;
}