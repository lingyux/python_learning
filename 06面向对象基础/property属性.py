# class Person(object):
#     def __init__(self):
#         self.__age = 18
#         pass

#     def get_age(self):
#         return self.__age

#     def set_age(self, age):
#         if age < 0:
#             print('年龄不能小于0')
#         else:
#             self.__age = age
#             pass
#         pass
#     age = property(get_age, set_age)

#     pass


# p1 = Person()
# print(p1.age)
# p1.age = -1
# print(p1.age)
# 实现方式2：通过装饰器
class Person(object):
    def __init__(self):
        self.__age = 18
        pass

    @property
    def age(self):
        return self.__age
        pass

    @age.setter
    def age(self, age):
        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age = age
            pass
        pass


p1 = Person()
print(p1.age)
p1.age = 30
print(p1.age)
