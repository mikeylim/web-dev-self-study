#include <stdio.h>
#include <string.h>
#define MAX_LENGTH 100


int isPalindrome() {
    char str[MAX_LENGTH];
    scanf("%s", str);
    int isPalindrome;
    for (int i = 0; i <= strlen(str) / 2; i++) {
        if (str[i] == str[strlen(str) - i - 1]) {
            isPalindrome = 1;
        } else {
            return 0;
        }
    }
    return isPalindrome;
}

int main() {
    
    printf("%d", isPalindrome());
    
    return 0;
    
}

