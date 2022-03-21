"""
@Author:沙漠丘吉尔

列表（List）是一种有序和可更改的集合。允许重复的成员。
"""
# 创建列表
thislist = ["apple", "banana", "cherry"]
print(thislist)

# 访问元素
# 1、通过引用索引号来访问列表项
print(thislist[0])
print(thislist[1])
print(thislist[2])
# print(thislist[3]) # 超出索引 报错IndexError: list index out of range

# 负的索引
print(thislist[-1])

# 索引范围
thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist1[2:5]) # 不包括末尾5

# 负索引的范围
print(thislist1[-4:-2])

# 通过索引更改元素值
thislist3 = ["apple", "banana", "cherry"]
thislist3[1] = "zhangxue"
print(thislist3)

#遍历元素
thislist4 = ["apple", "banana", "cherry"]
for i in thislist4:
    print(i)

# 检查元素是否存在
thislist5 = ["apple", "banana", "cherry"]
if "apple" in thislist5:
    print("Yes!")


# 获取列表长度
thislist6 = ["apple", "banana", "cherry"]
print(len(thislist6))
print(thislist6.__len__())

# 添加元素
thislist7 = ["apple", "banana", "cherry"]
thislist7.append("zhangxue")
print(thislist7)

# 指定的索引处添加元素
fruit = ["apple", "banana", "cherry"]
fruit.insert(0,"zhangxue")
print(fruit)


# 删除项目
# 1、删除指定的元素
fruit1 = ["apple", "banana", "cherry"]
fruit1.remove("apple")
print(fruit1)
# 1、删除指定的项目.如果删除的元素不存在,报错ValueError: list.remove(x): x not in list
# fruit3 = ["apple", "banana", "cherry"]
# fruit1.remove("zhangxue")
# print(fruit1)

# 根据索引删除项目，不填写索引，默认删除最后一项
fruit2 = ["apple", "banana", "cherry"]
print(fruit2.pop(1))  # 指定索引
print(fruit.pop()) # 不指定索引

# 删除列表.或者根据索引删除列表元素
fruit3 = ["apple", "banana", "cherry"]
del fruit3[1]
# print(fruit3) # NameError: name 'fruit3' is not defined


# 清空列表
fruit4 = ["apple", "banana", "cherry"]
fruit4.clear()
print(fruit4)

# copy() 方法来复制列表：
a = ["apple", "banana", "cherry"]
b = a.copy()
print(b)

# list() 强转为列表
a = ("apple", "banana", "cherry")
print(list(a))
print("=======================")
# 合并两个列表
list1 = ["a", "b" , "c"]
list2 = [1, "a", 3]
list3 = list1+list2 # 不去重
print(list1)
print(list2)
print(list3)
print("=======================")

# 追加的方式
a1 = ["a", "b" , "c"]
b1 = [1, "a", 3]

# 将a追加给b
for i in a1:
    b1.append(i)
print(b1)
print(a1)

#  extend() 方法追加
m = ["a", "b" , "c"]
n = [1, "a", 3]
n.extend(m)
print(n)
print(m)


# 倒叙reverse
w = ['apple', 'banana', 'cherry']
w.reverse()
print(w)

# sort 排序
# 返回值的长度的函数：
def myFunc(e):
  return len(e)
cars = ['Porsche', 'Audi', 'BMW', 'Volvo']
cars.sort(key=myFunc)
