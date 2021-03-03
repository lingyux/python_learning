class Person(object):
    def __init__(self, n, a):
        self.__name = n
        self.__age = a
        pass

    def __str__(self):
        return '{}的年龄是{}'.format(self.__name, self.__age)
        pass

    def getAgeInfo(self):
        return self.__age

    def setAge(self, age):
        if age > 0 and age < 120:
            self.__age = age
        else:
            print('您输入的数据不合法')
        pass

    def getNameInfo(self):
        return self.__name
        pass

    def setName(self, name):
        self.__name = name
