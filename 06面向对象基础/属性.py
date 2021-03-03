class Student(object):
    name = '李明'  # 属于类属性，就是student所拥有的属性

    def __init__(self, age):
        self.age = age
        pass
    pass


lm = Student(18)
Student.name = '刘德华'
print(lm.name)
print(Student.name)
# print(Student.age)不能访问
