#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    // each line until line number of n
    for (int i = 1; i <= n; i++) {
        // top spaces
        for (int j = n - i; j > 0; j--) {
		    printf(" ");
		}
        for (int k = 1; k <= 2 * i - 1; k++) {
            printf("*");
        }
        
        printf("\n");
    }
    for (int i = n - 1; i > 0; i--) {
        for (int j = n - i; j > 0; j--) {
            printf(" ");
        }
        for (int k = 0; k < 2 * i -1; k++) {
            printf("*");
        }
        // for (int k = 2 * i - 1; k > 0; k--) {
        //     printf("*");
        // }
        printf("\n");
    }
    
    
}