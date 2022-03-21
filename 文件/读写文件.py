"""
@Author:沙漠丘吉尔

open()
    模式：不能单独使用，默认不写，t模式
        t 文本模式
        b  二进制/bytes
    操作
        r 读文件
        w 写文件
        a 追加文件内容
        zhangxue:123456
zhangtao:123456
zhangaiwu:123456
zhouhan:123456
"""

# with 上下文
with open("b.txt","r",encoding="utf-8") as f1,\
        open("a.txt","r",encoding="utf-8") as f2:
    res = f1.read()
    res2 = f2.read()
    print(res)
    print(res2)