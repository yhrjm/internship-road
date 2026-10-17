#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int *p;
    int sum = 0;

    for (p = arr; p < arr + 5; p++) {
        sum += *p;
    }

    printf("%d\n", sum);
    return 0;
}
