Test = 'python'
# print(type(Test))
# for item in Test:
#     print(item, end='')
print('首字母变大写 %s' % Test.capitalize())
a = '     hello     '
b = a.strip()
print(a, '\n', b)
print(a.lstrip())
print(a.rstrip())
print('a的地址为%d' % id(a))  # id()的作用是查看对象的内存地址
print(a.find('l'))  # 查找第一个目标对象在序列对象中的位置,如果没有找到返回-1
print(a.index('lo'))  # 返回的为目标对象的下标值，检测不到报错，产生异常
print(a.startswith(' '))
print(a.endswith(' '))
print(a.upper())

# 排序
print(Test[::-1])
