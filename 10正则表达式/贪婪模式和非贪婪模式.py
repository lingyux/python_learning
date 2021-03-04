import re

# 贪婪模式
# 默认的匹配模式
# 在满足条件的情况下，尽可能多的匹配数据
res = re.match(r'\d{6,9}', '111222333')
print(res.group())

content = 'aacbacbc'
pattern = re.compile(r'a.*b')
result = pattern.search(content)
print('贪婪模式%s' % result.group())

content = 'aacbacbc'
pattern = re.compile(r'a.*?b')  # 非贪婪模式匹配
result = pattern.search(content)
print('非贪婪模式%s' % result.group())

# 非贪婪模式
# 在满足条件的情况下尽可能少的匹配数据
rs = re.match(r'\d{6,9}?', '111222333')
print(rs.group())
