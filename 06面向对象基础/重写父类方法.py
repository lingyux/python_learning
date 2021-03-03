class Dog(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def talk(self):
        print('wangwang')
        pass
    pass


class kejiquan(Dog):
    def __init__(self, name, color):  # 调用父类的方法
        # Dog.__init__(self, name, color)  # 重写父类的方法，执行完毕就可以具备父类的属性
        # 扩展其他的属性
        # 还可以利用super关键字
        super().__init__(name, color)  # 自动查找父类，自动调用方法
        # 如果继承了多个父类，那么会按照顺序诸葛的查找
        self.height = 90
        self.weight = 20

    def talk(self):  # 重写父类的方法
        super().talk()
        print('叫的跟狗一样')

    def __str__(self):
        return '{} {} {} {}'.format(self.name, self.color, self.height, self.weight)  # noqa: E501
    pass


kj = kejiquan('qt', 'red')
kj.talk()
print(kj)
