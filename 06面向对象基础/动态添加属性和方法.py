import types  # 导入添加方法的库


def dymicMethod(self):
    print('{}的体重是：{},学校是{}'.format(self.name, self.weight, Student.school))
    pass


@classmethod
def classTest(cls):
    print('这是一个类方法')
    pass


@staticmethod
def staticMethodTest():
    print('这是一个静态方法')
    pass


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def __str__(self):
        return '{}今天{}岁了'.format(self.name, self.age)
        pass


print('绑定类方法')
Student.Testmethod = classTest
Student.Testmethod()
print('绑定类方法执行结束')
print('绑定静态方法')
Student.TeststaticMethod = staticMethodTest
Student.TeststaticMethod()
print('静态方法执行结束')
Student.school = '南京大学'  # 动态添加类属性
zyh = Student('lingyux', 20)
print('实例调用类方法')
zyh.Testmethod()
zyh.weight = 80  # 动态添加属性
# 绑定方法
zyh.printInfo = types.MethodType(dymicMethod, zyh)
print(zyh)
print(zyh.weight)
zyh.printInfo()  # 调用动态绑定的方法
print('-'*30)
zm = Student('lingyuxia', 20)
print(zm)
# print(zm.weight)
print('-'*30)


print(zm.school)
print('-'*30)
# 动态添加实例方法
