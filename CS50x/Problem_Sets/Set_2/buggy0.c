#include <cs50.h>
#include <stdio.h>

// Constant
const int N = 3;

// Prototype
float average(int length, int array[]);

int main(void)
{
    // Scores
    int scores[N];
    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Score: ");
    }

    // Print the average
    printf("Average: %f\n", (scores[0] + scores[1] + scores[2])/3.0);
}

float average(int length, int array[])
{
    // Calculate Average
    // Initialize blank value
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        // Running total based on the values in the array
        sum += array[i];
    }
    // Divide the total by the length of the array, as a float
    return sum / (float) length;
}