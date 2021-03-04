
import re
# compile re模块中的编译方法 可以把一个字符串编译成一个字节码
# reobj = re.compile(r'\d{4}')
# # 开始使用模式对象
# res = reobj.match('123124')
# print(res.group())
# # print(re.match(r'\d{4}', '123124').group())

# # re.search 规则是：在全文中匹配一次，匹配到就返回
# data = '我爱伟大的祖国,I love China,China is a great country'
# res = re.search('China', data)
# print(res)
# print(res.group())
# print(data[15:20])

# # re.findall() 查询字符串中的某个正则表达式全部的非重复出现的情况，返回的是一个复合正则表达式的结果列表
# data = '毛主席是一位伟大的思想家,毛岸英是一位伟大的战士'
# res = re.findall('毛..', data)
# rsearch = re.search('毛..', data)
# print(rsearch)
# print(res)
#
# # 使用compile改造一下
# reObj = re.compile('毛..')  # 创建一个正则表达式对象
# print(reObj.search(data))
# print(reObj.findall(data))

# # re.subn 完成目标的搜素和替换并且返回被替换的数量 以元组的形式返回
# # re.sub 实现目标的搜索和替换
# data = 'Python是很受欢迎的编程语言Python是世界上最好的语言'
# pattern = '[a-zA-Z]+' # 字符集的范围 + 表示前导字符出现一次以上
# res = re.sub(pattern, 'C语言', data)
# resn = re.subn(pattern, 'C语言', data)
# print(res)
# print(resn)

# re.split 分割字符串
data = '百度,阿里,腾讯,华为,360'
res = re.split(',', data)
print(type(res))
print(res)
