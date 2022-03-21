"""
@Author:沙漠丘吉尔
"""
# 获取位置 1 处的字符（请记住第一个字符的位置为 0
result = 'hello world'
print(result[1])

# 获取从位置 2 到位置 5（不包括）的字符
print(result[2:5])

# 使用负索引从字符串末尾开始切片(不包含-2和后面的元素)
print(result[-5:-2])

# len() 函数返回字符串的长度：
print(len(result))


"""字符串的内置方法"""
# strip() 方法删除开头和结尾的空白字符：
res = " hello world "
print(res.strip())

# lower() 返回小写的字符串：
res1 = "HELLO WORLD"
print(res1.lower())

# islower() 判断是否返回小写字符串
print(res1.islower())

# upper() 方法返回大写的字符串：
res2 = "hello world"
print(res2.upper())

# isupper() 判断是否返回大写字符串
print(res2.isupper())

# replace() 用另一段字符串来替换字符串
a = "Hello, World!"
print(a.replace("World", "Kitty"))

# split() 方法在找到分隔符的实例时将字符串拆分为子字符串
a = "Hello, World!"
b = a.split(",")
print(type(b)) # 拆分后以列表的形式展现<class 'list'>


"""检查字符串中是否存在特定短语或字符，我们可以使用 in 或 not in 关键字"""
# 检查以下文本中是否存在短语 "ina"
txt = "China is a great country"
x = "China" in txt
print(x)
y = "zhangxue"
if y not in txt:
    print(y + "不在" + txt + "中")

"""字符串级联（串联）"""
# 将变量 a 与变量 b 合并到变量 c 中
a = "hello"
b = "world"
c = a + " " + b
print(c)

# 字符串无法和数字链接在一起，需要将数字转化为字符串
age = 63
txt = "My name is Bill, I am " + str(age)
print(txt)

# 或者使用格式化方法format()
age = 63
txt = "My name is Bill, I am {}"
print(txt.format(age))

# format 可以使用多个占位符，{}中不填写位子，按照顺序，填写位子，按照位置占位
quantity = 3
itemno = 567
price = 49.95
myorder = "dollars for {}。pieces of item {}.I want to pay {}。"
myorder1 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))
print(myorder1.format(quantity,itemno,price))

# count()	返回指定值在字符串中出现的次数
myorder2 = "dollars for。pieces of item .I want to pay。"
print(myorder2.count("i")) # 区分大小写

# endswith() 判断是否以指定的字符串结尾
d = "zhangxue is shuai"
if d.endswith("shuai"):
    print("是的")


# 	在字符串中搜索指定的值并返回它被找到的位置。
txt = "Hello, welcome to my world."
x = txt.find("welcome1") # 返回首字母的索引 ，找不到返回-1
print(x)

# index() 方法与 find() 方法几乎相同，唯一的区别是，如果找不到该值，则 find() 方法将返回 -1

# y = txt.index("welcome1") # 找不到报错ValueError: substring not found
# print(y)

# isdigit()如果字符串中的所有字符都是数字，则返回 True。
a = "131341414"
print(a.isdigit())

# join() 	把可迭代对象的元素连接到字符串的末尾。
a = ("zhangxue","zhangtao","zhangaiwu")
x = "#".join(a)
print(x)

# 使用单词 "TEST" 作为分隔符，将字典中的所有项目连接成一个字符串：
myDict = {"name": "Bill", "country": "USA"} # 链接的是key
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

# zfill()在字符串的开头填充指定数量的 0 值。
txt = "zhangxue" # 如果 len 参数的值小于字符串的长度，则不执行填充。

x = txt.zfill(10)

print(x)

