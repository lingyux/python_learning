import re
# # | 竖线 匹配左右任意一个表达式 实际上是一个或的关系
# string = 'lingyux8888'
# res = re.match('(lingyux8888|lingyux)', string)
# print(res.group())

# # (a,b) 分组匹配 将括号中的字符作为一个分组
# # 匹配电话号码 xxxx-1231241
# res = re.match(r'([0-9]*)-(\d*)', '0355-123114155')
# # ^ 有两种含义 1：以xxxx开头 2：否定 取反
# res = re.match(r'([^-]*)-(\d*)', '0355-123114155')
# print(res.group(0))
# print(res.group(1))
# print(res.group(2))

# # \num 的使用 引用分组num匹配到的字符串
# htmlTag = '<html><h1>测试数据</h1></html>'
# res = re.match(r'<(.+)><(.+)>(.+)</\2></\1>',  htmlTag)
# print(res.group(1))
# print(res.group(2))
# print(res.group(3))

# 分组别名的使用 (?P<name>)
# 使用别名：(?P=引用的名字)
data = '<div><h1>www.baidu.com</h1></div>'
res = re.match(r'<(?P<div>\w*)><(?P<h1>\w*)>(.*)</(?P=h1)></(?P=div)>', data)

print(res.group(0))
print(res.group(1))
print(res.group(2))
print(res.group(3))