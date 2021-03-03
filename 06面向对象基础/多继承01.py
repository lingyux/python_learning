# class shenxian:
#     def fly(self):
#         print('神仙都会飞')
#         pass
#     pass


# class Monkey:
#     def eat(self):
#         print('猴子喜欢吃桃')
#         pass
#     pass


# class Sunwukong(shenxian, Monkey):  # 既是神仙也是猴子

#     pass


# swk = Sunwukong()
# swk.eat()
# swk.fly()


class D(object):
    def eat(self):
        print('eat')
        pass
    pass


class C(D):
    def eat(self):
        print('C.eat')
        pass
    pass


class B(D):

    pass


class A(B, C):
    pass


a = A()
a.eat()  # 在执行eat()方法的查找顺序是
# 首先去A中查找，如果A中没有，则继续取B中查找，如果B中则取C类中查找，如果C类中没有，则取D类中查找，否则报错
print(A.__mro__)  # 查看类的查找顺序
