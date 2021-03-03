# # .的使用
import re
#
# data = 'aaaa'
# names = '李达', '李明', '小王', '小李'
# print(type(names))
# pattern = '李.'  # 匹配的规则
# # pattern = '..'  # 匹配除了换行符之外的所有字符
# for name in names:
#     res = re.match(pattern, name)
#     if res:
#         print(res.group())
#         pass
# []的使用 规则：匹配[]中的任意一个字符
# str1 = 'hello'
# # res = re.match('[he]', str1, re.I)
# # print(res.group())
# # parrern = '[abc]'  # 使用[]括起来的字符代表一个集合，代表匹配集合中的任意一个字符
# parrern = '[a-z]'  # 简写a-z的26个英文字母
# datas = 'a', 'b', 'c', 'd', 'wyw'
# for data in datas:
#     res = re.match(parrern, data)
#     if res:
#         print('匹配成功{}'.format(res.group()))


# # \d 匹配一个数字
# data = '12345abcdef'
# print(re.match('\d \d', data).group())
# # \D 匹配非数字
# data = 'd12345abcdef'
# print(re.match('\D', data).group())


# # \s 匹配空白字符或者tab
# data = ' hello'
# print(re.match('\s', data).group())
# # \S 匹配非空白的字符
# data = '1 hello'
# print(re.match('\S', data).group())

# \w 匹配单词字符，即a-z,A-Z,0-9,_
data = '2Yssdf'
print(re.match('\w\w', data).group())
# \W 匹配非单词的字符
data = '@#$2Yssdf'
print(re.match('\W\W', data).group())
