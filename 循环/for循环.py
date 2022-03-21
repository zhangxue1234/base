"""
@Author:沙漠丘吉尔

for 循环用于迭代序列（即列表，元组，字典，集合或字符串）。
"""
# 联合使用
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# 和range() 函数联合
# for i in range(10):
#     print(i)
# for x in range(10):
#     if x == 2:
#         break
#     print(x)
#
# for x in range(3, 10):# 不包含末尾数字,从0开始
#     print(x)

# for x in range(3, 50, 6):# 等差数列
#   print(x)

# for x in range(10):
#   print(x)
# else:
#   print("Finally finished!")

# 嵌套遍历
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#   for y in fruits:
#     print(x, y)

# 打印乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{j}x{i}={i*j}\t', end='')
#     print()
#
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}x{i}={i*j}\t', end='')
    print()