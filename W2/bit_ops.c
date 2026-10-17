#include <stdio.h>

int main() {
    unsigned char n = 0;

    n |= (1 << 3);              // 第3位置1
    printf("置位后：%d\n", n);   // 8

    if (n & (1 << 5)) {         // 判断第5位
        printf("第5位是1\n");
    } else {
        printf("第5位是0\n");
    }

    n &= ~(1 << 3);             // 第3位清0
    printf("清位后：%d\n", n);   // 0
    return 0;
}
