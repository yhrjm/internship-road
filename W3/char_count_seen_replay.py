s = input("请输入一段字符串:")
if not s:
    print("字符串为空")
else:
    seen = ""
    best_ch = ""
    best_n = 0
    for ch in s:
        if ch in seen:
            continue
        seen = seen + ch
        n = s.count(ch)
        print(f"{ch}出现{n}次")
        if n > best_n:
            best_n = n
            best_ch = ch
    print(f"出现最多的是 {best_ch},共{best_n}次")
