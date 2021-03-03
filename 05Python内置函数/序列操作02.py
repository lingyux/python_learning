# # zip() 就是用来打包的 会把序列中索引对应的元素存储为一个元祖对象
# s1 = ['a', 'b', 'c']
# s2 = ['你', '我', '他']
# print(zip(s1))
# print(list(zip(s1)))  # 压缩一个数据

# ziplist = zip(s1, s2)
# print(list(ziplist))


# def printBookInfo():
#     books = []  # 存储所有的图书信息
#     bookid = input('请输入图书的编号：每个以空格分隔')
#     bookName = input('请输入图书的书名：每个以空格分隔')
#     bookPos = input('请输入图书的位置：每个以空格分隔')
#     idlist = bookid.split(' ')
#     namelist = bookName.split(' ')
#     poslist = bookPos.split(' ')

#     bookInfo = zip(idlist, namelist, poslist)
#     for bookItem in bookInfo:
#         '''
#         遍历图书信息进行存储
#         '''
#         dictInfo = {'编号': bookItem[0], '书名': bookItem[1], '位置': bookItem[2]}
#         books.append(dictInfo)
#         pass
#     for item in books:
#         print(item)
#         pass
#     pass


# printBookInfo()


listObj = ['1', 'b', 'c']
for index, item in enumerate(listObj, 5):
    print(index, item)
    pass

dicObj = {}
dicObj['name'] = 'lingyux'
dicObj['hobby'] = 'sing'
dicObj['pro'] = 'art'

for index, item in enumerate(dicObj):
    print(index, item, end=' ')
    print(dicObj[item])
