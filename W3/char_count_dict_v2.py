s = input("请输入一段字符串:")
if not s:
    print("字符串为空")
else:
    d = {}
    for ch in s:
        d[ch] = d.get(ch, 0) + 1
    for ch, n in d.items():
        print(f"{ch}出现{n}次")
        best_ch = max(d, key=d.get)
    for ch, n in sorted(d.items(), key=lambda kv: kv[1], reverse=True):
        print(f"{ch}: {n}次")
    print("出现最多的是", best_ch, "出现", d[best_ch], "次")
