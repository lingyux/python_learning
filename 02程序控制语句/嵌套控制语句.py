score = int(input('请输入您的学分'))
if score > 10:
    grade = int(input('请输入您的成绩'))
    if grade > 80:
        print('恭喜您，你可以升级了')
        pass
    else:
        print('你还需要努力')
        pass
else:
    print('您的成绩也太差了')
