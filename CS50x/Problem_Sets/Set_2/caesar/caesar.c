#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    // Check for exactly one command line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Ensure the command-line argument is a non-negative integer
    for (int i = 0; n = strlen(argv[1]); i < n; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // Convert the key from string to integer
    int k = atoi(argv[1]);

    // Prompt user for plaintext
    string plaintext = get_string("plaintext: ");

    // Print the ciphertext
    printf("ciphertext: ");

    // Iterate over each character in the plaintext
    for (int i = 0; n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];

        // Check if the character is an uppercase letter
        if (isupper(c))
        {
            printf("%c", (c - 'A' + k) % 26 + 'A');
        }
        // Check if the character is a lowercase letter
        elif (islower(c))
        {
            printf("%c", (c - 'a' + k) % 26 + 'a');
        }
        // Else if it's not a letter, print the character as-is
        else
        {
            printf("%c", c);
        }
    }

    // Print a new line at the end
    printf("\n");
    
    // Return success
    return 0;
}