"""
@Author:沙漠丘吉尔

如果使用 while 循环，只要条件为真，我们就可以执行一组语句。
"""
# 只要 i 小于 7，打印 i：
# i = 0
# while i < 7:
#     print(i)
#     i += 1

# 如果永远不满足条件,则用会一直继续下去,应该可以用break
# i = 1
# while i < 7:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# continue 表示跳过后继续下一个程序
# i = 0
# while i < 7:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


# while ...else
i = 1
while i < 6:
  print(i)
  i += 1
else: # 当i = 6时,会走else程序
  print("i is no longer less than 6")
