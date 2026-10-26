s = input("请输入一段字符串：")
if not s:
    print("字符串为空")

s = s.strip()
parts = s.split()
s = "".join(parts)


def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


print(is_palindrome(s))
print(is_palindrome("level"))   # 应 True
print(is_palindrome("abca"))    # 应 False
print(is_palindrome("abcba"))   # 应 True
