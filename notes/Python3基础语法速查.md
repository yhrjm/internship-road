# Python 3 基础语法速查手册

> 按学习顺序编排 · 做题时随手查
> 适用版本：Python 3.x（Python 2 已于 2020 年停止维护）
> 用法：做题时随手查语法，逻辑自己写

## 1. 变量与类型

Python 的变量不用声明类型，直接赋值，类型自动推断，之后还能改。

```python
a = 10        # int 整数
b = 3.14      # float 小数
c = "你好"    # str 字符串（单双引号都行）
d = True      # bool 布尔（首字母大写）
e = None      # None 表示"什么都没有"
print(type(a))   # <class 'int'> 查看类型

x = int("42")      # 字符串转 int
y = str(42)        # int 转字符串
z = float("3.5")   # 字符串转 float
```

注意：`0`、`""`（空字符串）、`[]`（空列表）、`None` 在 if 里都算「假」，其余算「真」。

## 2. 输入与输出

```python
name = input("姓名：")        # input 读进来的永远是字符串！
age = int(input("年龄："))    # 要当数字用，必须 int() 转换
print(f"{name}今年{age}岁")   # f-string：引号前加 f，变量塞 {}
print(f"总分：{90 + 5}")      # {} 里可以放表达式
print(f"成绩：{88.456:.1f}")  # :.1f 保留 1 位小数 → 88.5
print("a", "b", sep="-")      # a-b   sep 控制间隔
print("不换行", end="")       # end 控制结尾（默认是换行）
```

新手第一坑：`input()` 拿的是字符串，`age + 1` 会报错，先 `int()`。

## 3. 运算符

| 运算 | 写法 | 例子 | 结果 |
|---|---|---|---|
| 加减乘 | `+ - *` | `7 * 3` | 21 |
| 除法（真除） | `/` | `7 / 2` | 3.5（永远是 float！） |
| 整除 | `//` | `7 // 2` | 3 |
| 取余 | `%` | `7 % 2` | 1 |
| 幂 | `**` | `2 ** 10` | 1024 |
| 比较 | `== != > < >= <=` | `3 == 3` | True |
| 逻辑 | `and or not` | `a > 1 and a < 9` | 写单词，不是符号 |
| 成员判断 | `in / not in` | `"a" in "abc"` | True |
| 自增 | `i += 1` | 没有 `i++` 这种写法，只能 `+=` | |

## 4. 分支 if / elif / else

```python
score = 85
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("重修")
# 注意：冒号！每行结尾的冒号表示"接下来是一个代码块"
# 代码块靠缩进区分（4 个空格），缩进错 = 逻辑错
```

## 5. 循环

```python
for i in range(5):        # 0,1,2,3,4（左闭右开，不含 5）
    print(i)
for i in range(1, 101):   # 1 到 100
    pass
for i in range(0, 10, 2): # 0,2,4,6,8（第三个参数是步长）
    pass

n = 0
while n < 5:
    n += 1
# break 跳出整个循环；continue 跳过本轮进入下一轮
```

for 遍历容器（Python 特色，极高频）：

```python
for ch in "hello":        # 逐个字符
    print(ch)
for item in [10, 20, 30]: # 逐个元素
    print(item)
```

## 6. 字符串

```python
s = "hello world"
s[0]            # 'h' 索引从 0 开始
s[-1]           # 'd' 负数从尾巴数
s[0:5]          # 'hello' 切片 [起:止]，含头不含尾
s[::-1]         # 反转 'dlrow olleh'
len(s)          # 11 长度
s.split(" ")    # ['hello', 'world'] 按分隔符切开成列表
",".join(["a","b"])  # 'a,b' 用逗号拼接
s.strip()       # 去掉首尾空白（换行、空格）
s.replace("world", "python")  # 替换
s.startswith("he")  # True
s.upper()       # 'HELLO WORLD'
"a" in s        # 子串判断
```

记住：字符串不可变，所有方法都返回新字符串，原串不动。

## 7. 列表 list

有序的容器，什么类型都能装，长度随时变。

```python
a = [3, 1, 4, 1, 5]
a.append(9)   # 尾部追加 → [3,1,4,1,5,9]
a.remove(1)   # 删掉第一个值为 1 的 → [3,4,1,5,9]
a.pop()       # 弹出最后一个
a[0] = 99     # 按下标改
a.sort()      # 原地排序（升序）
sorted(a)     # 返回新列表，原列表不动
len(a)        # 长度
5 in a        # 是否存在
a[1:3]        # 切片，同字符串
a.reverse()   # 原地反转

# 遍历的两种姿势
for x in a:
    print(x)
for i, x in enumerate(a):  # 既要下标又要值
    print(i, x)
```

## 8. 字典 dict

键值对容器：用「键」找「值」，查找飞快。解析接口返回的数据全靠它。

```python
d = {"name": "张三", "age": 20}
d["name"]            # '张三' 按键取值（键不存在会报 KeyError）
d.get("score", 0)    # 键不存在时返回默认值 0，不报错 ★安全取法
d["score"] = 88      # 新增或修改
del d["age"]         # 删除
"name" in d          # 判断键是否存在
d.keys() / d.values() / d.items()

# 遍历
for k, v in d.items():
    print(k, v)

# 计数套路（字符统计题的核心）：
d[c] = d.get(c, 0) + 1
```

## 9. 函数

```python
def add(a, b):
    return a + b    # return 返回结果；不写就返回 None

def greet(name, prefix="你好"):   # 默认参数：不传就用默认值
    return f"{prefix}，{name}"

greet("张三")            # '你好，张三'
greet("张三", "早上好")  # 覆盖默认值
add(1, 2)              # 3
```

亮点：不用声明返回类型和参数类型；还能一次返回多个值 `return a, b`，接收时 `x, y = f()`。

## 10. 文件读写

```python
# 写
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")

# 读
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:            # 逐行读
        print(line.strip())   # strip 去掉行尾换行
```

记住：`with` 块结束自动关文件；`"w"` 会清空原内容，追加用 `"a"`；中文务必加 `encoding="utf-8"`。

## 11. 异常（程序不崩的护身符）

```python
try:
    age = int(input("年龄："))
except ValueError:
    print("请输入数字")    # 输入字母也不崩

try:
    f = open("不存在的文件.txt")
except FileNotFoundError:
    print("文件不存在，创建新文件")
```

核心思想：先假设会出错，把「出了错怎么办」提前写好——程序就有了防御力。

## 12. 模块与第三方库

```python
import random
random.randint(1, 100)   # 随机整数 1~100（闭区间！）

from math import sqrt    # 只导入需要的函数
sqrt(16)                 # 4.0

# 安装第三方库（在终端/命令行里执行，不是代码）：
# pip install requests   以后发网络请求用
# pip install pytest     以后写测试用
```

## 13. 附录：最容易踩的 8 个坑

1. `input()` 返回字符串，算术前先 `int()`
2. 冒号：if / for / while / def / try 行尾都要冒号
3. 缩进是语法：同一代码块必须对齐，混用 Tab 和空格会报错
4. `range(1, 101)` 不含 101——左闭右开
5. `7 / 2 = 3.5`（不是 3）；要整数用 `//`
6. 字符串不可变：`s[0] = "H"` 会报错，要用方法生成新串
7. `=` 是赋值，`==` 才是比较（if 里写错不会报语法错，但逻辑全错）
8. 列表 `b = a` 不是复制，是同一个列表的两个名字；复制用 `b = a.copy()` 或 `b = a[:]`
