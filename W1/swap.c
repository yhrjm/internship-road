#include <stdio.h>

void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int main() {
    int x = 1, y = 2;
    printf("交换前：x=%d, y=%d\n", x, y);
    swap(&x, &y);
    printf("交换后：x=%d, y=%d\n", x, y);
    return 0;
}
