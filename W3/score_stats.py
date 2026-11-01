s = input()
if not s.strip():
    print("没有输入成绩")
else:
    parts = s.split()
    nums = []
    for p in parts:
        nums.append(int(p))
    print(f"人数：{len(nums)}")
    print(f"总分：{sum(nums)}")
    print(f"平均分：{sum(nums)/len(nums):.1f}")
    print(f"最高分：{max(nums)}")
    print(f"最低分：{min(nums)}")
