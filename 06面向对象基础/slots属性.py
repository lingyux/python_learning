# 作用：
# 限制要添加的实例属性
# 节约内存空间
class Student(object):
    __slots__ = ('name', 'age', 'score')

    def __str__(self):
        return '{} {} {}'.format(self.name, self.age, self.score)

    pass


xw = Student()
xw.name = 'xw'
xw.age = 10
xw.score = 96
# print(xw.__dict__)  # 所有的数据都存放在字典里，但是占用空间较大
# 在定义了__slots__变量之后，student类已经不能随意创建不在__slots__范围内的属性了
print(xw)

# 在继承关系中的使用
# 子类未声明 __slots__属性的时候，子类不会继承父类的__slots__
# 子类声明__slots__，子类会继承父类的__slots__属性
# 子类的__slots__范围是自身的范围加上父类的范围


class subStudent(Student):

    __slots__ = ('gender', 'pro')
    pass


lm = subStudent()
lm.gender = '男'
lm.pro = 'computer'
print(lm.gender, lm.pro)
