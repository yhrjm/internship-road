a = [3, 1, 4, 1, 6, 7, 3, 23, 54, 33, 55, 22]
uniq = []
for x in a:
    if x not in uniq:
        uniq.append(x)
print(uniq)
s = sorted(uniq)
print(s)
top3 = s[-3:]
print(top3)
print(set(a))            # 直接去重，但顺序乱了
print(sorted(set(a)))    # 对比手写的版本
