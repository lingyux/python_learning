class Animal(object):
    def __eat(self):
        print('eat')
        pass

    def run(self):
        self.__eat()  # 在此调用私有化方法
        print('run')
        pass
    pass


class Bird(Animal):
    pass


b1 = Bird()
b1.run()
b1.eat()
