#include <stdio.h>

int negyzet(int a) {
    int szam = 0;
    printf("%d\n", szam);
    return a * a;
}

int main(void) {
    int szam = 17;
    printf("%d\n", negyzet(2));
    return 0;
}