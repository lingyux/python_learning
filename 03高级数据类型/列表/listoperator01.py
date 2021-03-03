li = [1, 2, 3, '你好']
print(len(li))

print(type(li))
listA = ['abcd', 785, 12.23, '取值', True]

print(listA)  # 输出整个列表
print(listA[0])  # 输出第一个元素
print(listA[1:3])  # 输出第二项到第三项元素
print(listA[2:])  # 输出从第三项至最后一项元素
print(listA[::-1])  # 负数表示倒叙输出
print(listA*2)  # 输出多次次列表
print('----------常用的函数----------')
print('追加之前的数据', listA)
listA.append(['fff', 'ddd'])  # 追加的列表
listA.append(8888)
print('追加之后的数据', listA)
listA.insert(1, '这是我插入的字符串')  # 指定位置插入数据
print(listA)
rsData = list(range(10))  # 强制转换成list对象
print(type(rsData))
listA.extend(rsData)  # 批量变价，扩展
listA.extend([11, 22, 33, 44])
print(listA)
print('----------修改list----------')
print('修改之前之前的数据', listA)
listA[0] = 'lingyux'

print('修改之后', listA)
listB = list(range(10, 50))
print('----------删除操作----------')
print(listB)
# del listB[0]  # 删除列表中的元素

del listB[1:3]  # 通过切片批量删除多个数据

listB.remove(20)  # 移除指定的元素具体的数据值
listB.pop(0)  # 可以移除指定项 参数为索引值
print(listB)

print(listB.index(19))  # 返回的是索引下标
