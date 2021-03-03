# 需要先去定义一个角色类
class Role(object):
    def __init__(self, name, hp):
        '''
        初始化构造函数
        name:角色姓名
        hp：角色血量
        '''
        self.name = name
        self.hp = hp
        pass

    def tong(self, enemy):
        # 捅一刀
        # 敌人扣掉10滴血
        enemy.hp -= 10
        info = '{}捅了{}一刀'.format(self.name, enemy.name)
        print(info)

        pass

    def kanren(self, enemy):
        enemy.hp -= 15
        info = '{}砍了{}一刀'.format(self.name, enemy.name)
        print(info)
        pass

    def chiyao(self):
        self.hp += 10
        info = '{}吃了一颗补血药丸，增加了10滴血'.format(self.name)
        print(info)
        pass

    def __str__(self):
        return '{}还剩下{}滴血'.format(self.name, self.hp)


# 创建两个实例化对象
xmcx = Role('西门吹雪', 100)
ygc = Role('叶孤城', 100)
while True:
	if xmcx.hp <= 0 or ygc.hp <= 0:
        break  # noqa: E117
        pass
    xmcx.tong(ygc)  # 西门吹雪捅了叶孤城一刀
    print(xmcx)  # 打印状态
    print(ygc)
    print('*********************')
    ygc.tong(xmcx)
    print(xmcx)  # 打印状态
    print(ygc)
    print('*********************')
    xmcx.chiyao()
    print(xmcx)  # 打印状态
    print(ygc)
    print('*********************')

print('对战结束')
