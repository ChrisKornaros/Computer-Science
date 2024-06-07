#include <stdio.h>

int main() {
    int height = 5;

    for (int i = 1; i <= height; i++) {
        // Print spaces
        for (int j = 0; j < height - i; j++) {
            printf(" ");
        }
        // Print hashes
        for (int k = 0; k < i; k++) {
            printf("#");
        }
        // Move to the next line
        printf("\n");
    }

    return 0;
}
