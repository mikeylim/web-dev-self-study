#include <stdio.h>

int main() {
    int numInput;
    int count;
    char strInput[100];
    scanf("%d", &numInput);
        

    for (int i = 0; i < numInput; i++) {
        scanf("%s", strInput);
        for (count = 0; strInput[count] != '\0'; ++count);
        printf("%c%c\n", strInput[0], strInput[count-1]);
    }
}