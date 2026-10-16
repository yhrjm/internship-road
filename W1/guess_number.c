#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));              // 播种：全程序只播一次
    char again = 'y';
    while (again == 'y') {          // 外层循环：再来一局
        int answer = rand() % 100 + 1;
        int guess, count = 0;       // 每局重新计数

        while (1) {                 // 内层循环：单局猜数
            printf("猜一个1-100的数：");

            // ★补丁：防止输入字母死循环
            // scanf 成功读到数字返回1，读到字母失败返回0
            while (scanf("%d", &guess) != 1) {
                printf("输入无效，请输入数字！\n");
                while (getchar() != '\n');  // 逐个吃掉缓冲区里卡住的字母
            }

            count++;
            if (guess > answer)      printf("大了\n");
            else if (guess < answer) printf("小了\n");
            else {
                printf("对了！用了%d次\n", count);
                break;
            }
        }

        printf("再来一局？(y/n): ");
        scanf(" %c", &again);       // %c 前的空格：吃掉残留回车
    }
    printf("游戏结束\n");
    return 0;
}
