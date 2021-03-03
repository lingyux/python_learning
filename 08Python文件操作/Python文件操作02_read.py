# 读取数据
fobj = open('test.txt', 'r', encoding='utf-8')  # 需要指定编码格式
# a = fobj.read() #读取所有数据
# print(a)
b = fobj.read(12)
print(b)
# 第二次读取会从第一次读取的末尾开始读取
print(fobj.readline())  # 读取一行
print(fobj.readlines())  # 读取的是一个列表
fobj.close()


# 读取数据
fobj = open('test01.txt', 'rb')  # 需要指定编码格式
# a = fobj.read() #读取所有数据
# print(a)
b = fobj.read(12)
print(b.decode('utf-8'))
# 第二次读取会从第一次读取的末尾开始读取
print(fobj.readline())  # 读取一行
print(fobj.readlines())  # 读取的是一个列表
fobj.close()
# with的使用 自动释放对象
with open('test.txt', 'a', encoding='utf-8') as f:
    # print(f.read())
    f.write('oh my god')
