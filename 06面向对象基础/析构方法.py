class Animal:
    def __init__(self, name):
        self.name = name
        print('这是构造初始化方法')
        pass

    def __del__(self):
        print('当在某个作用域下面没有被引用的情况下，解释器会自动的调用此函数')
        print('这是析构方法')
        print('{}这个对象被彻底清理了'.format(self.name))
        pass


cat = Animal('ketty')
del cat  # 手动删除对象
input('程序等待中')
print('*'*29)

dog = Animal('柯基')
