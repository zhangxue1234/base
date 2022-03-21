"""
@Author:沙漠丘吉尔
Person 类
"""

# 初始化函数__init__() 函数

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Bill", 63)
p1.myfunc()

p1.age = 40
print(p1.age)