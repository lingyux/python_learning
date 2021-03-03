class ToolongMyException(Exception):
    def __init__(self, length):
        self.len = length
        pass

    def __str__(self):
        return '您输入的姓名数据长度是'+str(self.len)+'超出规定长度'
        pass
    pass


def name_test():
    name = input('请输入您的姓名')
    try:
        if len(name) > 5:
            raise ToolongMyException(len(name))
            pass
        else:
            print(name)
            pass
        pass
    except ToolongMyException as msg:
        print(msg)
        pass
    finally:
        print('函数执行完毕')


name_test()
