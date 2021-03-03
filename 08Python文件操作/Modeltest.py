
__all__ = ['add', 'sub']
# __all__魔术变量的作用是 如果在一个文件中存在__all__变量，那么就意味着这个变量中的元素会被from import导入所有的时候会被导入
# 对于import方法来说无论__all__有没有都会被导入


def add(x, y):
    return x+y
    pass


def sub(x, y):
    return x-y
    pass


def printInfo():
    return '这是一个自定义方法'


# 测试
if __name__ == '__main__':
    res = add(3, 4)
    print('3+4={}'.format(res))
    print('模块__name__变量{}'.format(__name__))
