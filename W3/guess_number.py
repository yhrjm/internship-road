import random


def make_answer(low=1, high=100):
    return random.randint(low, high)


def judge(guess, answer):
    if guess == answer:
        return "猜对了"
    elif guess > answer:
        return "大了"
    else:
        return "小了"


def main():
    answer = make_answer()
    k = 1
    count = 0
    while k:
        guess = int(input("请输入你猜的数字："))
        count += 1
        result = judge(guess, answer)
        print(result)
        if result == "猜对了":
            break
    print(f"共猜了{count}次")


main()
