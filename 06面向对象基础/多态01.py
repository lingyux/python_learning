# 父类
class Animal(object):
    def say_who(self):
        print('我是一个动物')
        pass
    pass

# 子类


class Duck(Animal):

    def say_who(self):
        print('我是一只鸭子')
        pass
    pass


class Dog(Animal):
    def say_who(self):
        print('我是一只狗')
        pass
    pass


def commonInvoke(obj):
    '''
    统一调用的方法
    '''
    obj.say_who()


# duck1 = Duck()
# duck1.say_who()
# dog1 = Dog()
# dog1.say_who()
listObj = [Duck(), Dog()]
for item in listObj:
    commonInvoke(item)
