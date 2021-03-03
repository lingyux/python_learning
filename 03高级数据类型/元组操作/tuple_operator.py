tupleA = ()  # 空元组
print(id(tupleA))
tupleA = ('abcd', 12, 9.12, 'lingyux', [11, 22, 33])
print(id(tupleA))
print(tupleA)
print(type(tupleA))
# 元组的查询
for item in tupleA:
    print(item, end=' ')
    pass
    print()
print(tupleA[2:4])

print(tupleA[::-1])
print(tupleA[::-2])  # 表示反转字符串每隔两个取一次
print(tupleA[-2:-1:])
tupleA[4][1] = 1231232
print(tupleA)
tupleC = (1, 2, 3, 1, 12, 32)
print(tupleC.count(1))  # 可以统计元素出现的次数
