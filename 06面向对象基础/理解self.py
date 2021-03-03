class Person(object):
    """docstring for Person"""

    def eat(self, name, food):
        # print(self)
        # print('self={}'.format(id(self)))
        print('{} 喜欢吃 {}'.format(name, food))
        pass
    pass


# xw是一个新的实例化对象
xw = Person()

xw.eat('lingyux', 'fish')
print('xw={}'.format(id(xw)))
