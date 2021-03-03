
# 写一个函数，检查传入字典的每一个value的长度，如果长度大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
# 字典中value只能是字符串或列表


def dict_func(dictparms):
    reslut = {}
    for key, value in dictparms.items():
        if len(value) > 2:
            reslut[key] = value[:2]
            pass
        else:
            reslut[key] = value
            pass
        pass
    return reslut
    pass


# 函数调用
dictObj = {'name': 'lingyux', 'hobby': ['唱歌', '跳舞', '运动', '编程'], 'pro': '艺术专业'}

print(dict_func(dictObj))
