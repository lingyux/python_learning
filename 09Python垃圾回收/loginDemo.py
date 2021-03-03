# import sys
import argparse

# print('参数的个数为：', len(sys.argv), '个参数')
# print('参数列表：', str(sys.argv[1:]))


# 创建一个解析器对象
parse = argparse.ArgumentParser(prog='系统登陆', usage='%(prog)s [options] usage',
                                description='系统系定义命令行文件', epilog='my - epilog')
# 添加必选参数
parse.add_argument('loginType', type=str, help='登陆系统类型')

# 添加可选参数
# parse.add_argument('-s', '--sex', action='append',type=str, help='你的性别')

# 限定范围
parse.add_argument('-u', dest='user', type=str, help='你的用户名')
parse.add_argument('-p', dest='pwd', type=str, help='你的密码')
# print(parse.print_help())
result = parse.parse_args()  # 开始解析参数
# print(result.name, result.age, result.sex)
if result.user == 'root' and result.pwd == '123456':
    print('登陆成功')
    pass
else:
    print('登录失败')
    pass
