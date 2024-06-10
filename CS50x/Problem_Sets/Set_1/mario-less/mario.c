#include <cs50.h>
#include <stdio.h>

int main() {
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1);

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
