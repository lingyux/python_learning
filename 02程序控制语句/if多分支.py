score = float(input('请输入你的分数:\n'))
if score < 60:
    print('不及格')  # noqa: W191
    pass  # noqa: W191
elif score >= 60 and score < 70:
    print('及格')  # noqa: W191
    pass  # noqa: W191
elif score >= 70 and score < 80:
    print('中')  # noqa: W191
    pass  # noqa: W191
elif score >= 80 and score < 90:  # noqa: E225
    print('良')  # noqa: W191
    pass  # noqa: W191
else:
    print('优')  # noqa: W191
    pass  # noqa: W191
print('语句执行结束')  # noqa: W292
