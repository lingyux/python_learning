def sum(*args):
    sum = 0
    for item in args:
        sum += item
        pass
    return sum
    pass


result = sum(1, 2, 3, 4, 5)
# result1 = sum(list(range(1, 20)))
# result1 = sum(range(20))
print('result={}'.format(result))
# 返回列表或元组的奇数项数据 返回值类型为新的列表


def data_process(con):
    listNew = []
    index = 1
    for item in con:
        if index % 2 == 1:
            listNew.append(item)
            pass
        index += 1
        pass
    return listNew
    pass


initData = list(range(10, 30))
print(initData)
rs = data_process(list(range(10, 30)))
print(rs)


# def dictFunc(dictParms):
#     '''
#     处理字典类型的数据
#     返回字典
#     '''
#     result2 = {}  # 空字典
#     for item in dictParms.items():  # key-value
#         if len(value) > 2:
#             result2[key] = value[:2]  # 向字典添加数据
