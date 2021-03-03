# 0:石头SublimeCodeIntel 1：剪刀 2：布
import random
count = 1
while count < 10:
    person = int(input('请出拳:0:石头 1：剪刀 2：布\n'))
    computer = random.randint(0, 2)
    computer1 = '拳头'
    if computer == 0:
        computer1 = '拳头'
        pass
    elif computer == 1:
        computer1 = '剪刀'
        pass
    elif computer == 2:
        computer1 = '布'
        pass
    print('电脑出的是：%s\n' % computer1)
    if person > 2:
        print('无效数据')
        pass
    elif person == 0 and computer == 0:
        print('平手')
        pass
    elif person == 0 and computer == 1:
        print('你赢了')
        pass
    elif person == 0 and computer == 2:
        print('你输了')
        pass
    elif person == 1 and computer == 0:
        print('你输了')
        pass
    elif person == 1 and computer == 1:
        print('平手')
        pass
    elif person == 1 and computer == 2:
        print('你赢了')
        pass
    elif person == 2 and computer == 0:
        print('你赢了')
        pass
    elif person == 2 and computer == 1:
        print('你输了')
        pass
    elif person == 2 and computer == 2:
        print('平手')
        pass
    count += 1
