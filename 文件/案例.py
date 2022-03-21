ipt_username = input("请输入用户名：").strip()
ipt_password = input("请输入密码：").strip()

with open(r"db.txt","r",encoding="utf-8") as f:
    for res in f:
        username,password = res.strip().split(":")
        if ipt_username == username and ipt_password == password:
            print("登录成功")
            break
    else:
        print("登录失败")