def fun1():
    print('---------------fun1 start---------------')
    print('---------------执行代码省略---------------')
    print('---------------fun1 end---------------')
    pass


def fun2():
    print('---------------fun2 start---------------')
    fun1()
    print('---------------fun2 end---------------')
    pass


fun2()  # 调用函数2
