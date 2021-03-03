# 返回指针当前所在的位置
# with open('test01.txt', 'r', encoding='utf-8') as f:
#     print(f.read(3))
#     print(f.tell())
#     print(f.read(2))
#     print(f.tell())
# with open('test01.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
#     pass
# print('截取之后的数据')
# with open('test01.txt', 'r+', encoding='utf-8') as f:
#     f.truncate(15)
#     print(f.read())


with open('test01.txt', 'rb') as f:
    data = f.read(2)
    print(data.decode('utf-8'))
    f.seek(-2, 1)  # 相当于光标向前移动2个字节
    print(f.read(4).decode('utf-8'))
    f.seek(-6, 2)
    print(f.read(6).decode('utf-8'))
