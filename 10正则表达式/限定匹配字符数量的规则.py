# # *  匹配前一个字符出现0次或者无限次，即可有可无
import re

#
# # res=re.match('[A-Z][A_Z]*','My') 匹配0次
# # res = re.match('[A-Z][a-z]*', 'Mny')#匹配两次
# res = re.match('[A-Z][a-z]*', 'Anyeverydayishappy')  # 可以匹配无限次
# print(res.group())

# # + 匹配前一个字符出现1次或者无限次,至少匹配一次
# res = re.match('[a-zA-Z]+', 'mYnameislingyux')
# # 匹配复合规范[不能以数字开头只能包含字母和下划线]的python变量名
# res = re.match('[a-zA-Z_]+[\w]*', 'name')
# res = re.match('[a-zA-Z_]+[\w]*', '_na99me')
# res = re.match('[a-zA-Z_]+[\w]*', '_na99me')
# print(res.group())

# # ? 告诉匹配引擎匹配前导字符0次或者一次，事实上表示前导字符是可以选择的可以有也可以没有
# res = re.match('[a-zA-Z_]+[0-9]?', 'na99me')
# print(res.group())

# {min,max} 告诉匹配引擎匹配前导字符min次到max次，min和max必须为非负整数
# {count} 表示精确匹配count位数字
# {min,} max省略的话表示最大值没有限制
# res=re.match('\d{4,}','1234567890')
# res = re.match('\d{4,8}', '1234567890')
# if res:
#     print('匹配成功 {}'.format(res.group()))
#     pass
# else:
#     print('匹配失败')
#     pass

# # 匹配邮箱 格式xxxxxx@163.com
# regexMail = re.match('[a-zA-Z0-9]{6,11}@163.com', 'lingyux910@163.com')
# regexTele = re.match('[1-9][0-9]{10}','08852057838')
# if regexTele:
#     print(regexTele.group())
# if regexMail:
#     print(regexMail.group())
# print(re.match('c:\\\\a.txt','c:\\a.txt').group())
# print(re.match(r'c:\\a.txt', 'c:\\a.txt').group())  # 可以在正则前面加上r，表示原生的字符串，python解释器就不会转义了


# # ^ 匹配字符串的开头
# # res = re.match('^P.*','Python is a language')
# res = re.match(r'^P\w{5}', 'Python is a language')
# if res:
#     print(res.group())

# $ 匹配结尾
res = re.match(r'[\w]{6,15}@[\w]{2,5}.com$', 'lingyux910@gmail.com')
if res:
    print(res.group())
    pass
