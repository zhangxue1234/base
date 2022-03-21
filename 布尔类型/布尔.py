"""
@Author:沙漠丘吉尔
"""
print(bool("Hello"))

print("=====================")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print("=====================")
# 一个值或对象的计算结果为 False，即如果对象由带有 __len__ 函数的类生成的，且该函数返回 0 或 False
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

# isinstance() 该函数可用于确定对象是否具有某种数据类型
# 判断x是否为int类型的整数
x = 200
print(isinstance(x, int))
