s = "hello world"

seen = ""
best_ch = ""
best_n = 0

for ch in s:
    if ch in seen:
        continue
    seen += ch
    n = s.count(ch)
    print(ch, "出现", n, "次")
    if n > best_n:
        best_ch = ch
        best_n = n

print("最多的是", best_ch, "共", best_n, "次")
