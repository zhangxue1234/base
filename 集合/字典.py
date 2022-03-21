"""
@Author:沙漠丘吉尔


字典（Dictionary）是一个无序，可变和有索引的集合。没有重复的成员。
"""
# 创建字典
thisdict =	{
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}
print(thisdict)

# 1 根据key访问value
x = thisdict["brand"]
print(x)

# 通过get()方法,获取value值
print(thisdict.get("brand"))


# 更改值

thisdict =	{
  "brand": {"Porsche":1},
  "model": "911",
  "year": 1963
}
thisdict["brand"]["Porsche"] = 2019
print(thisdict)


print("===================")
# 遍历字典
thisdict1 =	{
  "brand": {"Porsche":1},
  "model": "911",
  "year": 1963
}
thisdict1["brand"]["Porsche"] = 2019
for x in thisdict1: # 遍历key值
  print(thisdict1[x])


print("===================")
# 方式一 遍历values值,
thisdict2 =	{
  "brand": {"Porsche":1},
  "model": "911",
  "year": 1963
}
# 方式1
for i in thisdict2:
    print(thisdict2.get(i))
# 方式2
for i in thisdict2.values():
    print(i)

print("===================")
# 方式三 使用 items() 函数遍历键和值：
for x,y in thisdict2.items():
  print(x,y)


# 检查字典中是否存在 "model"
thisdict3 =	{
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}
if "model" in thisdict3:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# 打印字典长度
print(len(thisdict))


# 添加元素
thisdict =	{
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}
thisdict["color"] = "red"
print(thisdict)


# 删除项目
# pop() 方法删除具有指定键名的项
thisdict4 =	{
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}
thisdict4.pop("year")
# popitem() 删除最后的元素
thisdict4.popitem()
print(thisdict4)


# del 删除整个字典,不存在就报错


# fromkeys 拥有指定key-value的字典
# 创建拥有 3 个键的字典，值均为 0：

x = ('key1', 'key2', 'key3')
y = 0
thisdict7 = dict.fromkeys(x, y)
print(thisdict7)

# value返回None
x = ('key1', 'key2', 'key3')
thisdict8= dict.fromkeys(x)
print(thisdict8)