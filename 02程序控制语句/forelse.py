account = 'admin'
pwd = 'admin'

for i in range(3):
    zh = input('请输入您的账号：')
    pd = input('请输入您的密码：')
    if account == zh and pwd == pd:
        print('恭喜你登陆成功！')
        break
        pass
    else:
        print('您输入的账号或密码错误，请重新输入：')
    pass
else:
    print('您的账号已经被锁定！')
