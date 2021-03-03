# class People(object):
#     country = 'China'

#     @classmethod  # 类方法
#     def get_country(cls):
#         return cls.country  # 访问类属性
#         pass

#     @classmethod
#     def change_country(cls, data):
#         cls.country = data
#         pass

#     @staticmethod
#     def print_country():
#         print('静态方法{}'.format(People.country))
#         pass
#     pass


# print(People.get_country())
# xm = People()
# print('实例对象访问{}'.format(xm.get_country()))
# People.change_country('English')
# print(People.get_country())
# People.print_country()  # 一般情况下，不会通过实例对象访问静态方法


import time  # 引入时间模块


class TimeTest(object):
    @staticmethod
    def show_time():
        return time.strftime("%H:%M:%S", time.localtime())
        pass
    pass


print(TimeTest.show_time())
