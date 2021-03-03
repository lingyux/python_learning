pro = '计算机信息管理'


def printInfo():
    name = 'lingyux'
    print('{} {}'.format(name, pro))
    pass


def TestMethod():
    name = 'lingyuxia'
    print(name)
    print(pro)
    pass


printInfo()
TestMethod()


def changeGlobal():
    '''
    修改全局变量
    '''
    global pro  # 修改全局变量，如果函数内部没有global关键字，则修改的内容被视为局部变量
    pro = '市场营销'
    print(pro)
    pass


changeGlobal()
print(pro)
