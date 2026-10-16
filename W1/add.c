#include <stdio.h>

void add(int *a, int *b, int *result) {
    *result = *a + *b;
}

int main() {
    int x = 3, y = 4, sum = 0;
    add(&x, &y, &sum);
    printf("sum=%d\n", sum);
    return 0;
}
