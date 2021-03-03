a = 100
b = 100
print(id(a))
print(id(b))


class Person(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        pass

    def say(self):
        print('我的名字是{}，今年{}岁，体重{}，身高{}'.format(self.name, self.age, self.weight, self.height))
        pass

    pass


def add(x, y):
    '''
    加法计算
    :param x:
    :param y:
    :return:
    '''
    return x + y


print(add(10, 20))
