dictA = {"pro": '电子信息', "school": '南京工业大学'}  # 空字典
# 添加字典数据
dictA['name'] = 'lingyux'  # name 代表key
dictA['age'] = '30'
dictA['pos'] = '小说家'
print(dictA)  # 输出完整的字典
print(len(dictA))  # 字典长度
print(type(dictA))

print(dictA['name'])  # 通过键获取对应的值
dictA['name'] = 'lingyuxia'  # 修改键对应的值

dictA.update({'pro': '计算机'})
dictA.update({'height': '180'})  # 可以添加或修改
print(dictA['name'])
# 获取所有的键
print(dictA.keys())
# 获取所有的值
print(dictA.values())
# 获取所有的键值对
print(dictA.items())

for key, value in dictA.items():
    print('%s==%s' % (key, value))

# 删除操作
del dictA['name']  # 通过指点键进行删除
dictA.pop('age')
print(dictA)
# 排序 按照key排序
print(sorted(dictA.items(), key=lambda d: d[0]))
# 按照 value 排序
print(sorted(dictA.items(), key=lambda d: d[1]))
