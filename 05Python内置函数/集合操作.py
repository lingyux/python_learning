# set 不支持索引和切片，是一个无序的且不重复的容器
# 类似于字典，但是没有value 只有key
dic1 = {1: 3}
set1 = {1, 2, 3}
# print(type(set1))
# print(type(dic1))
# 集合添加
set1.add('python')
print(set1)
# 集合清空
set1.clear()
print(set1)

a = {12, 32, 23}
b = {12, 32, 44, 23}
# 差
print(b.difference(a))
print(b-a)
# 交集
print(a.intersection(b))
print(a & b)
# 并集
print(a.union(b))
print(a | b)
# 随机移除数据 pop没有参数
deldata = b.pop()
print(b)
print(deldata)
# 直接指定移除数据
print(a.discard(12))

print(a.update(b))
