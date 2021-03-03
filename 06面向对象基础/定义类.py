class Person:
    # 属性
    name = 'lingyux'  # 类属性
    # age = 22

    def __init__(self):
        self.name = 'lingyuxia'  # 实例属性
        self.age = 20
        pass
    # 方法

    def eat(self):
        print('大口吃饭')
        pass

    def run(self):
        print('飞速的跑')
        pass


# 创建对象[类的实例化]
xm = Person()
xm.eat()  # 调用函数
xm.run()
# xm.age = 20
print('{}的年龄是{}'.format(xm.name, xm.age))
