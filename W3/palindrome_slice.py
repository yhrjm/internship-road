def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("level"))   # 应 True
print(is_palindrome("abca"))    # 应 False
print(is_palindrome("abcba"))   # 应 True
