#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main(){
    int tamMat, i, j, x, y;

    x = 0;

    while(1){
        scanf("%d", &tamMat);
        if (tamMat == 0 || !tamMat) break;
        for (i = 1; i <= tamMat; ++i){
            x = i;
            for (j = y = 1; j <= tamMat; ++j){
                if(j != 1) printf(" ");
                if (j >= i){printf("%3hd", y); y++;} else {printf("%3hd", x); x--;}
            }
            printf("\n");
        }
        printf("\n"); 
    }
    return 0;
}