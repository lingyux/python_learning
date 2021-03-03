# 创建一个单例对象 基于__new__方法实现
class DataBaseClass(object):
    def __new__(cls, *args, **kwargs):
        # cls._instance=cls.__new__(cls)
        # 不能使用自身的new方法，会造成迭代死循环
        if not hasattr(cls, '_instance'):  # 如果不存在就创建
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class DBoptSignle(DataBaseClass):
    pass


db1 = DataBaseClass()
db2 = DataBaseClass()
db3 = DataBaseClass()
print(id(db1))
print(id(db2))
print(id(db3))
db1 = DBoptSignle()
db2 = DBoptSignle()
db3 = DBoptSignle()
print(id(db1))
print(id(db2))
print(id(db3))
