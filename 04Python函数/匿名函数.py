def computer(x, y):
    '''
    计算数据的和
    '''
    return x+y
    pass


print(computer(10, 24))


def M(x, y): return x+y


# 通过变量调用匿名函数
print(M(12, 32))


def result(a, b, c): return a*b*c


print(result(12, 24, 52))


age = 15
print('可以参军' if age > 18 else '继续上学')


def funcTest(x, y): return x if x > y else y
# funcTest=lambda x,y:x if x>y else y


print(funcTest(12, 2))

rs = (lambda x, y: x if x > y else y)(16, 12)

print(rs)
