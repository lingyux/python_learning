# 序列操作：str,元组，列表
print(all([]))
print(all([1, 2, 3, False]))


print(any((0, False, 1)))


# sort && sorted
li = [2, 3, 12, 1, 32, 10]
# li.sort()  # list自带的排序方法直接修改的是也是对象
print('排序之前{}'.format(li))
# sort只能用于列表排序
li0 = sorted(li, reverse=True)  # 默认为False 升序排列
print(li0)

tupArray = (1, 32, 23, 55, 22, 10)
tupArray01 = sorted(tupArray)
print(tupArray01)


# reverse反转排序

# range 创建一个整数列表
