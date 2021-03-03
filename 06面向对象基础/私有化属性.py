class Person(object):
    __hobby = 'dance'  # 私有类属性

    def __init__(self):
        self.__name = 'lingyux'  # 加上__将此属性私有化 类的内部可以访问
        self.age = 22
        pass

    def __str__(self):
        return '{} is {} years old,he likes {}'.format(self.__name, self.age, self.__hobby)  # noqa: E501
        pass

    def changeValue(self):
        Person.__hobby = 'sing'


class student(Person):

    def printInfo(self):
        print(self.__name)
    pass


lingyux = Person()
# print(lingyux.__name)  # 通过类对象进行外部访问
# 私有化之后不能再外部直接访问
lingyux.changeValue()
print(lingyux)
print(lingyux.hobby)
print('*'*20)
stu = student()
print(stu)
print(stu.__name)  # 属性不能被子类继承，但是可以通过父类的方法进行访问

stu.printInfo()
