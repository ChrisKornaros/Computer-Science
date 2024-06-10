#include <stdio.h>
#include <cs50.h> 

void print_row(int spaces, int bricks);
void mirror_row(int spaces, int bricks);

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    for (int i = 0; i < n; i++)
    {
        print_row(n, i);
        printf("  ");
        mirror_row(n, i);
        printf("\n");
    }
}

void print_row(int spaces, int bricks)
{
    // Print Spaces
    for (int i = spaces - 1; i > bricks; i--)
    {
        printf(" ");
    }
    // Print Bricks
    for (int j = spaces - bricks; j <= spaces; j++)
    {
        printf("#");
    }
}

void mirror_row(int spaces, int bricks)
{
    // Print Bricks
    for (int j = spaces - bricks; j <= spaces; j++)
    {
        printf("#");
    }
}
