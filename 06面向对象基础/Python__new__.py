class Animal(object):
    def __init__(self):
        self.color = 'red'
        pass
        # 在python当中，如果不重写 ，new方法的默认结构如下

    def __new__(cls, *args, **kwargs):
        return super().__new(cls, *args, **kwargs)
        return object.__new(cls, *args, **kwargs)
    pass


tiger = Animal()  # 实例化的过程会自动调用new方法创建实例
