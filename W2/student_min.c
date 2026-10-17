#include <stdio.h>

struct Student {
    char name[10];
    int id;
    float score;
};

int main() {
    struct Student cls[3] = {
        {"学生1", 1, 100.44f},
        {"学生2", 2, 343.33f},
        {"学生3", 3, 423.33f}
    };

    int low = 0;
    for (int i = 1; i < 3; i++) {
        if (cls[i].score < cls[low].score) {
            low = i;
        }
    }

    printf("最低分：%s 学号%d\n", cls[low].name, cls[low].id);
    return 0;
}
