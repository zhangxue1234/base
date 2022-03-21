"""
@Author:沙漠丘吉尔

元组（Tuple）是一种有序且不可更改的集合。允许重复的成员。
"""
# 创建元组
res = ("apple", "banana", "cherry","cherry")

# 根据索引访问元组元素
res1 = ("apple", "banana", "cherry","cherry")
print(res1[1])

# 更改元组元素，元组不可更改，可以先将元组转为为list，后燃更改后在转化为元组
res2 = ("apple", "banana", "cherry","cherry")
y = list(res2)
y[1] = "zhangxue"
res2 = tuple(y)
print(res2)


print("======================")
# 遍历元组

res3 = ("apple", "banana", "cherry","cherry")
for i in res3:
    print(i)

# 检查项目是否存在
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# 元组长度
print(len(thistuple))

# 创建一个元素的元组，后面需要加逗号,否则就是字符串
x = ("a",)
print(type(x))

# 删除元组
del x

print("===================")
# 合并元组
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# 元组方法
# 1、index()，组中搜索指定的值并返回它被找到的位置。
# 2、count(). 返回元组中指定值出现的次数。









