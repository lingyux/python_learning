# 求皆乘

def jicheng(n):
    result = 1
    for item in range(1, n+1):
        result *= item
        pass
    return result
    pass


print('5的阶乘为{}'.format(jicheng(5)))


# 递归方式实现
def diguiJc(n):
    '''
    递归方式实现阶乘函数
    '''
    if n == 1:
        return 1
    else:
        return n*diguiJc(n-1)
    pass

# 递归调用


print('递归调用阶乘{}'.format(diguiJc(5)))
