import psutil
import os
import gc
print(gc.get_threshold())


def showmemsize(tag):
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024 / 1024
    print('{}memory used:{}MB'.format(tag, memory))

    pass


# 验证循环引用的情况
def func():
    showmemsize('初始化')
    a = [i for i in range(100000)]
    b = [i for i in range(100000)]
    a.append(b)
    b.append(a)
    showmemsize('创建列表对象a b之后')
    pass


func()
gc.collect()  # 手动释放
showmemsize('完成时候的')
