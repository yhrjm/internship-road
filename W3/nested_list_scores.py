scores = [[90, 85, 77], [60, 70, 80], [92, 88, 95]]
avgs = [sum(row) / len(row) for row in scores]
for i, a in enumerate(avgs):
    print(f"学生{i} 平均分：{a:.1f}")
best = max(max(row) for row in scores)
print(f"全班最高分：{best}")
