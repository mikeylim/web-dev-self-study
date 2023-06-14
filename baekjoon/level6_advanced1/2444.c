#include <stdio.h>

int main() {
    int numStars;
    scanf("%d", &numStars);

    // each line until line number of numStars
    for (int i = 1; i <= numStars; i++) {
        // top spaces
        for (int j = numStars - 1; j >= 0; j--) {
            // printf("\nj: %d\n", j);
            printf(" ");
        }
        for (int k = 1; k <= 2*i-1; k++) {
            printf("*");
        }
        printf("\n");
    }
    
}