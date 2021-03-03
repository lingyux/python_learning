# def sumRange(m, n):
#     '''
#     求从m到n的连续自然数的总和
#     '''
#     return sum(range(m, n+1))
#     pass


# print(sumRange(1, 10))
# print(sumRange(20, 30))
# print(sumRange(35, 45))


# def person_sount():
#     '''
#     计算有多少个和尚
#     假设大和尚有a个，小和尚有100-n个
#     '''
#     for a in range(1, 100):
#         if(a*3+(100-a)/3) == 100:
#             # 100个和尚吃100个馒头
#             return (a, 100-a)
#         pass
#     pass


# rsObj = person_sount()
# print('大和尚有{}个人，小和尚有{}个人'.format(rsObj[0], rsObj[1]))
li = [1, 3, 4, 3, 3, 5, 2, 4, 2, 1, 7, 5]
set1 = set(li)
print(set1)
for i in set1:
    li.remove(i)
    pass
set2 = set(li)  # set2中存储的数据就是li中有重复的数据集合
print(set1-set2)
for i in set1:
    if i not in set2:
        print(i)
        pass
    pass
