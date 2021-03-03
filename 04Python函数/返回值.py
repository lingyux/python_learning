def sum(a, b):
    sum = a+b
    return sum  # 将计算结果返回
    pass


result = sum(10.6, 30)  # 将返回值赋给其他的变量
print(result)
print(sum(10, 30))  # 函数的返回值返回到调用的地方


def caluate_computer(num):
    li = []
    result = 0
    i = 1
    while i <= num:
        result += i
        i += 1
        pass
    li.append(result)
    return li
    pass


value = caluate_computer(10)
print(value)
print(type(value))


def returnTuple():
    # return 1, 2, 3
    return {'name': 'lingyux', 'age': 10}
    pass


a = returnTuple()
print(type(a))
