"""
@Author:沙漠丘吉尔

集合（Set）是一个无序和无索引的集合。没有重复的成员。
由于集合是无序的，因此，不能根据索引查找，且不能重复,如果重复，不会报错，但是会去掉后面相同的元素
"""
#
# # 创建集合
# thisset = {"apple", "banana", "cherry"}
# print(thisset)
#
#
# # 遍历集合
# for x in thisset:
#   print(x)
#
# # 可以新增集合，但是无法修改
# # 1、新增 add()
# thisset1 = {"apple", "banana", "cherry"}
# thisset1.add("orange")
# print(thisset1)
#
# # 使用 update() 方法将多个项添加到集合中
# thisset2 = {"apple", "banana", "cherry"}
# thisset2.update(["orange", "mango", "grapes"])
# print(thisset2)
#
# # 获取 Set 的长度
# thisset3 = {"apple", "banana", "cherry"}
# print(len(thisset3))
#

# 删除项目
# 1、使用 remove() 方法来删除，如果不存在就报错
thisset4 = {"apple", "banana", "cherry","apple"}
thisset4.remove("apple")
print(thisset4)


print("============================================")
# 2、discard()方法删除元素不会报错
thisset5 = {"apple", "banana", "cherry","apple"}
thisset5.discard("apple")
print(thisset5)
thisset5.discard("zhangxue")
print(thisset5)


# pop()方法的返回值是被删除的元素。随机删除
thisset6 = {"apple", "banana", "cherry","apple"}
print(thisset6.pop())
print(thisset6)


# clear() 清空集合
# union() 和 update() 都将排除任何重复项。
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
















