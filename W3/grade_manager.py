def show_all(students):
    for s in students:
        print(f"{s['name']}:{s['score']}")


def add_students(students):
    name = input("姓名：").strip()
    if not name:
        print("姓名不能为空")
        return
    try:
        score = int(input("分数："))
    except ValueError:
        print("分数必须是数字，本次录入作废")
        return
    students.append({"name": name, "score": score})


def show_stats(students):
    if not students:
        print("暂无成绩")
        return
    scores = [s["score"] for s in students]
    print(f"人数：{len(scores)} 平均：{sum(scores)/len(scores):.1f} "
          f"最高{max(scores)}最低{min(scores)}")


def main():
    students = [
        {"name": "张三", "score": 85},
        {"name": "李四", "score": 72},
        {"name": "王五", "score": 88},
    ]
    while True:
        print("\n1.录入2.查看3.统计4.退出")
        choice = input("选择：").strip()
        if choice == "1":
            add_students(students)
        elif choice == "2":
            show_all(students)
        elif choice == "3":
            show_stats(students)
        elif choice == "4":
            break
        else:
            print("没有这个选项")


main()
