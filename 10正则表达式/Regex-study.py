# 通过python中的re模块学习使用正则表达式的基本知识点
import re

data = 'Python is the best language in the world'
# res = re.match('python', data, re.I)  # 精确匹配 re.I表示忽略大小写
res = re.match('(.*) is (.*?) .*', data, re.I | re.M)
if res:
    print('匹配成功')
    print(res)
    print(res.groups())
    print(res.group(1))
    print(res.group(2))
    pass
else:
    print(res)
    print('匹配失败')
