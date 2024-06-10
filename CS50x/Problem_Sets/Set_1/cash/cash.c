#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Prompt user for change owed, in cents
    int n;
    do
    {
        n = get_int("Change: ");
    }
    while (n < 0);
    // Calculate how many quarters you should give the customer
    // Subtract the value of those quarters from cents
    int q = n / 25;
    n = n - (q * 25);

    // Calculate how many dimes you should give the customer
    // Subtract the value of those dimes from cents
    int d = n / 10;
    n = n - (d * 10);

    // Calculate how many nickles you should give the customer
    // Subtract the value of those nickles from cents
    int k = n / 5;
    n = n - (k * 5);

    // Calculate how many pennies you should give the customer
    // Subtract the value of those pennies from cents
    int p = n / 1;
    n = n - (p * 1);

    int coins = q + d + k + p;
    printf("%i\n", coins);
}
