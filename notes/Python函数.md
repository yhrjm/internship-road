# Python 函数

> def 定义调用 · 参数 · return · 默认参数 · 作用域
> 附练习：猜数字游戏的三函数拆分（含参考答案）。

## 一、为什么要学函数

程序从上到下「一坨」执行，二十行还能忍，两百行改一处 bug 要翻半天。函数就是**给一段代码起个名字，以后随叫随到**。它解决三件事：

1. **复用**——同一段逻辑写一次，想调几次调几次；
2. **好读**——主流程只剩几行「干什么」，细节收进函数里；
3. **好改**——bug 出在哪个功能，就只改哪个函数，不动其他地方。

测试开发岗位里，一个测试脚本往往要重复执行几十条用例，函数是把「重复劳动」变成「调一下」的基本功。

## 二、定义与调用：def

定义一个函数只要记住四件事：def、名字、括号、冒号加缩进。

```python
def say_hi():
    print("你好")

say_hi()    # 调用，输出：你好
say_hi()    # 再叫一次，又输出：你好
```

两个新手最容易栽的点：

1. **定义不等于执行**。def 只是「登记」，程序跑过 def 那几行时什么也不会发生，只有写 say_hi() 才真正执行里面的代码。
2. **调用必须带括号**。只写 say_hi 不带括号，等于「提了一下这个名字」，函数不会跑。

函数命名规则和变量名一样：字母、数字、下划线，不能以数字开头。缩进固定 4 个空格，函数体里每一行都要缩进。

## 三、参数：把数据递进去

```python
def add(a, b):
    print(a + b)

add(3, 5)      # 输出 8
add(10, 20)    # 输出 30
```

两个名词分清楚：

| 名词 | 位置 | 含义 | 例子 |
|---|---|---|---|
| 形参 | def 那一行的括号里 | 占位用的名字，等别人递值进来 | `def add(a, b)` 里的 a、b |
| 实参 | 调用那一行的括号里 | 真正递进去的值 | `add(3, 5)` 里的 3、5 |

传递规则是**按位置对号入座**：add(3, 5) 里 3 给 a、5 给 b，顺序不能乱；实参个数必须和形参个数一致（除非形参有默认值）。

## 四、return：把结果交出来

新手最常犯的错误就是把 print 和 return 混为一谈。一句话区分：**print 是给人看的，return 是给程序用的**。

```python
def add(a, b):
    return a + b

result = add(3, 5)   # add 算出 8，用 return 交出来，result 接住
print(result * 2)    # 16，拿到的结果还能继续参与计算
```

如果 add 里写的是 print(a + b)，屏幕上也能看到 8，但 result 接住的是 None，下一步 result * 2 直接报错——因为打印出来的数字只是「显示」，程序手里什么也没留下。

| 对比项 | print | return |
|---|---|---|
| 作用 | 把内容显示到屏幕上 | 把结果交回调用处 |
| 谁能用 | 只有人眼能看到 | 代码可以接住并继续计算 |
| 执行后 | 函数继续往下跑 | 函数立刻结束，后面代码不再执行 |

另外记住两条：return 一执行，函数立刻结束，写在它后面的代码都是废话；函数如果从头到尾没写 return，它默认返回 None。

## 五、默认参数：不写就用默认值

给形参一个「出厂设置」，调用时不递值就用默认值。

```python
import random

def make_answer(low=1, high=100):
    return random.randint(low, high)

print(make_answer())        # 不递值，默认在 1~100 里出题
print(make_answer(1, 10))   # 递了值，就改成在 1~10 里出题
```

规则只有一条：**带默认值的参数必须排在普通参数后面**。`def f(a=1, b)` 这种写法是语法错误。

## 六、作用域：函数里的变量出不来

```python
def test():
    x = 10      # x 是 test 的局部变量
    print(x)

test()
print(x)        # 报错：NameError，外面根本不认识 x
```

函数内部定义的变量叫**局部变量**，出了这个函数就消失。函数之间想交换数据，只有两条正规通道：**靠参数传进去，靠 return 拿出来**。这条规矩保证了改一个函数不会弄坏另一个。

## 七、练习：猜数字游戏的三函数拆分

把猜数字游戏拆成 3 个函数——**出题**、**判断**、**主循环**。要求：至少 1 个默认参数，至少 1 个函数有返回值。

分工设计：

| 函数 | 职责 | 输入（参数） | 输出（返回值） |
|---|---|---|---|
| make_answer | 出题：随机生成答案 | 范围（用默认参数） | 答案数字 |
| judge | 判断：比较猜的数和答案 | guess、answer | 「大了」/「小了」/「猜对了」 |
| main | 主循环：读输入、调判断、数次数 | 无 | 无（负责打印） |

骨架：

```python
def make_answer(范围带默认值):
    生成答案并 return

def judge(guess, answer):
    比较大小，return 结果文字

def main():
    answer = make_answer()
    进入循环:
        读用户输入
        result = judge(猜的数, answer)
        打印 result
        猜对就 break
    打印总次数

main()
```

## 八、新手五个坑

1. **定义了忘调用**：写完 def 就运行，屏幕空空如也——文件末尾记得写 main()。
2. **把 print 当 return**：屏幕上明明有结果，函数外一接却是 None——要给程序用的结果，必须 return。
3. **return 缩进写错**：return 缩进了 if 里面，变成「只有某种情况才返回」，其他情况函数返回 None——检查 return 的缩进层级。
4. **默认参数放前面**：`def f(a=1, b)` 是语法错误——默认参数一律靠后站。
5. **跨函数直接拿变量**：在 main 里想用 judge 的内部变量——此路不通，用参数递进去、用 return 拿回来。

## 答案区：参考实现

```python
import random

def make_answer(low=1, high=100):
    # 出题：在 [low, high] 范围内随机选一个整数
    return random.randint(low, high)

def judge(guess, answer):
    # 判断：返回猜测结果
    if guess > answer:
        return "大了"
    elif guess < answer:
        return "小了"
    else:
        return "猜对了"

def main():
    answer = make_answer()      # 用默认范围 1~100
    count = 0
    while True:
        guess = int(input("请输入你猜的数字："))
        count += 1
        result = judge(guess, answer)
        print(result)
        if result == "猜对了":
            break
    print(f"共猜了 {count} 次")

main()
```

自查点：三个函数分工清晰 ✓；make_answer 带默认参数 ✓；make_answer 和 judge 都有返回值且被接住 ✓。
