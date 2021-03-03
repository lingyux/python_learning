# tags = '我是一个中国人'  # 字符串类型本身就是一个字符类型的集合
# for item in tags:
#     print(item, end='')
#     pass
sum = 0
for data in range(1, 100, 2):
    print(data, end=' ')
    pass
print()
for data in range(1, 101):
    sum += data
    pass
print('sum = {}'.format(sum))
