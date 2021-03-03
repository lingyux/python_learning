def sum(a, b):  # 形式参数：形参只是意义上的一种参数，在定义的时候是不占用内存空间的
    sum = a+b
    print(sum)
    pass


# 函数的调用 在调用的时候是必须要赋值的
sum(20, 15)  # 20和15就是实际参数，简称实参 占用内存地址
sum(20.5, 30)


def sum1(a=20, b=30):  # 始终存在于参数列表的尾部
    print('默认参数的使用=%.1f' % (a+b))
    pass


# 默认参数的调用
sum1()
sum1(10)
sum1(20.5, 20.6)


def get_computer(*args):
    '''
    可变长的参数类型
    计算累加和
    '''
    # print(args)
    result = 0
    for item in args:
        result += item
    pass
    print('result=%d' % result)


get_computer(1, 2)
get_computer(1, 2, 3, 4, 5, 6)


def keyFunc(**kwargs):
    print(kwargs)
    pass


# 调用
dictA = {'name': 'Leo', 'age': 22}
keyFunc(**dictA)
keyFunc(name='peter', age=22)


def complex_func(*args, **kwargs):
    print(args)
    print(kwargs)
    pass


complex_func(1, 2, 3, 4, name='lingyux')
