"""
@Author:沙漠丘吉尔

"""
# 无参函数
# def my_function():
#   print("Hello from a function")
# my_function()
#
# def my_function1(y,z):
#     return y + z
# res = my_function1(1,2)
# print(res)

# 默认参数,调用时可以不用传参数,也可以传参数
# def my_function2(country = "China"):
#   print("I am from " + country)
# my_function2()
# my_function2("zhangxue")


# 以 List 传参,定义一个参数,可以传字符串,list,

# def my_function(food):
#   for x in food:
#     print(x)
# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

# 关键字参数
# def my_function(child3):
#   print("The youngest child is " + child3)
# my_function(child3 = "Rory")

# # 任意参数a
# def my_function(*kids):
#   print("The youngest child is " + kids[2])
#
# my_function("Phoebe", "Jennifer", "Rory")

# 任意参数a
# def my_function(**kwargs):
#   print(kwargs)
#
# my_function(a=1, b=3, c=3)


# 递归
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result
tri_recursion(6)