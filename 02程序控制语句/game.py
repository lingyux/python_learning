import random
count = 0
while True:
    age = random.randint(1, 10)
    number = int(input('请输入您猜测的数字：'))
    if(number == age):
        print('您猜对了')
        break
        pass
    else:
        count += 1
        pass
    if(count == 3):
        key = input('您已经失败，继续游戏请按y')
        if key == 'y':
            continue
            pass
        else:
            break
