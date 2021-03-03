class Grandfather(object):
    def eat(self):
        print('eat')
        pass
    pass


class Father(Grandfather):
    pass


class Son(Father):
    pass


son = Son()
son.eat()
print(Son.__mro__)
