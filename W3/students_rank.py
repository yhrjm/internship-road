students = [
    {"name": "张三", "chinese": 90, "math": 85},
    {"name": "李四", "chinese": 58, "math": 72},
    {"name": "王五", "chinese": 92, "math": 88},
]

maxman = 0
maxer = None
for stu in students:
    cur = stu["chinese"] + stu["math"]
    if cur > maxman:
        maxman = cur
        maxer = stu
print(maxer["name"], maxman)

rank = sorted(students, key=lambda s: s["chinese"] + s["math"], reverse=True)
for i, s in enumerate(rank):
    print(f"第{i+1}名 {s['name']}  {s['chinese']+s['math']}")

passed = len([s for s in students if s["chinese"] >= 60])
print(f"语文及格率：{passed / len(students):.0%}")
