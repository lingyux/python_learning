class Animal:
    def eat(self):
        print('eat somthing')
        pass

    def drink(self):
        print('drink somthing')
        pass
    pass


class Dog(Animal):
    def talk(self):
        print('小狗汪汪叫')
        pass

    pass


class Cat(Animal):
    def talk(self):
        print('小猫喵喵叫')
        pass
    pass


d1 = Dog()
d1.eat()

c1 = Cat()
c1.eat()
c1.talk()
