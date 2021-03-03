
# try:
#     print(b)  # 捕获逻辑的代码
#     # li = [1, 2, 34]
#     # print(li[10])
#     # a = 10/0
#     pass
# # except NameError as msg:
# #     # 捕获到错误才会到这里执行
# #     print(msg)
# #     pass
# # except IndexError as msg:
# #     print(msg)
# #     pass
# # except ZeroDivisionError as msg:
# #     print(msg)
# #     pass
# except Exception as result:
#     print(result)
# print('初次接触到异常')

def A(s):
    return 10/int(s)
    pass


def B(s):
    return A(s)*2
    pass


def main():
    try:
        B('0')
        pass
    except Exception as msg:
        print(msg)
        pass
    pass


# main()

# try:
#     print('aa')
#     pass
# except Exception as msg:
#     print(msg)
# else:
#     print('当try没有错误的情况下，执行此代码')


try:
    int('34')
    open('aaa.txt')
    pass
except Exception as msg:
    print(msg)
    pass
finally:
    print('不管有没有出错都会执行的代码')
