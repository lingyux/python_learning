class Person(object):
    """docstring for Person"""

    def __init__(self,  name, food, pro):
        self.name = name
        self.food = food
        self.pro = pro
        print('---init---函数已执行')
        pass

    def __str__(self):
        return '我是{} 是{}专业,喜欢吃 {}'.format(self.name, self.pro, self.food)

    def __new__(cls, *args, **kwargs):
        '''
        每调用一次就会生成一个新的对象
        场景：可以控制创建对象的一些属性限定，通常用于单例模式的时候使用 
        '''
        print('---new---函数已执行')
        return object.__new__(cls)  # 在这里是真正创建对象实例的函数
        pass

    def eat(self):
        # print(self)
        # print('self={}'.format(id(self)))
        print('{} 喜欢吃 {}'.format(self.name, self.food))
        pass
    pass


# xw是一个新的实例化对象
lingyux = Person('lingyux', 'fish', 'act')

print(lingyux)
