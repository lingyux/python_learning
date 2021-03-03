# coding = utf-8
# 打开文件
# 默认的编码是gdk 中文编码，最好的习惯就是指定一个编码
fobj = open('./test.txt', 'w', encoding='utf-8')  # 模式和C语言基本一致
# 读取/写入数据 已经存在，会将其覆盖
fobj.write('在苍茫的大海上\n')
fobj.write('狂风卷积着乌云\n')
fobj.close()  # 保存关闭文件


# 以二进制的方式写入
fobj01 = open('test01.txt', 'wb')  # str -> bytes
fobj01.write('在乌云和大海之间\n'.encode('utf-8'))
fobj01.close()

fobj01 = open('test.txt', 'a', encoding='utf-8')  # a追加
fobj01.write('在乌云和大海之间\n')
fobj01.write('海燕像黑色的闪电\n')
fobj01.close()


# 二进制字节追加
# 以二进制的方式写入
fobj01 = open('test01.txt', 'ab')  # str -> bytes
fobj01.write('在乌云和大海之间'.encode('utf-8'))
fobj01.close()
