s = "hello world"
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1
print(d)

max_ = max(d, key=d.get)
print("最多的是", max_, "共", d[max_], "次")
