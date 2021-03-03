import pygame  # 引用第三方的模块
import random  # 随机生成一个数据
from pygame.locals import *
'''
1.实现飞机的显示，并且可以控制飞机的移动
'''
# 抽象出一个基类


class BasePlane(object):
    def __init__(self, screen, imagePath):
        self.screen = screen
        self.image = pygame.image.load(imagePath)
        self.bulletList = []
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        # 完善子弹的展示逻辑
        needDelItem = []
        for item in self.bulletList:
            if item.judge():
                needDelItem.append(item)
                pass
            pass
        # 重新遍历一下
        for i in needDelItem:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()  # 显示一下子弹的位置
            bullet.move()  # 子弹进行移动 下次在显示的话就会看到子弹在修改后的位置了

    pass


class Basebullet(object):
    def __init__(self, x, y, screen, bulletType):
        self.type = bulletType
        self.screen = screen
        if self.type == 'hero':
            self.x = x + 13
            self.y = y-20
            self.imagepath = './feiji/bullet.png'
            pass
        elif self.type == 'enemy':
            self.x = x
            self.y = y + 10
            self.imagepath = './feiji/enemybullet.png'
            pass
        self.image = pygame.image.load(self.imagepath)
        pass

    def move(self):
        if self.type == 'hero':
            self.y -= 2
            pass
        elif self.type == 'enemy':
            self.y += 2
            pass
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def judge(self):
        if self.y > 500 or self.y < 0:
            return True
            pass
        else:
            return False
            pass
        pass
    pass


class HeroPlane(BasePlane):
    def __init__(self, screen):
        '''
        初始化对象
        screen:主窗体对象
        '''
        # 设定飞机的默认位置
        self.x = 150
        self.y = 450
        super().__init__(screen, './feiji/hero.png')  # 调用父类的方法
        pass

    def moveLeft(self):
        '''
        左移动
        '''
        if self.x > 0:
            self.x -= 10
        pass

    def moveRight(self):
        '''
        右移动
        '''
        if self.x < 350-40:
            self.x += 10
        pass

    # 发射子弹

    def shoot(self):
        newbullet = Basebullet(self.x, self.y, self.screen, 'hero')
        self.bulletList.append(newbullet)
        pass

    pass


def key_control(heroObj):
    '''
    定义普通的函数实现键盘的检测
    '''
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print('退出')
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.type == K_a or event.key == K_LEFT:
                print('left')
                heroObj.moveLeft()  # 调用函数实现左移动
                pass
            elif event.type == K_d or event.key == K_RIGHT:
                print('right')
                heroObj.moveRight()  # 调用函数实现右移动
                pass
            elif event.key == K_SPACE:
                print('space')
                heroObj.shoot()
                pass
            pass

# 创建子弹类


# 创建敌机
class Enemy(BasePlane):
    def __init__(self, screen):
        # 默认设置一个方向
        self.direction = 'right'
        self.x = 0
        self.y = 0
        super().__init__(screen, './feiji/enemy.png')
        pass

    def shoot(self):
        # 敌方随机发射子弹
        num = random.randint(1, 20)
        if num == 3:
            newBullet = Basebullet(self.x, self.y, self.screen, 'enemy')
            self.bulletList.append(newBullet)
        pass

    def move(self):
        # 随机移动
        if self.direction == 'right':
            self.x += 2
            pass
        elif self.direction == 'left':
            self.x -= 2
            pass
        if self.x > 350-20:
            self.direction = 'left'
            pass
        elif self.x < 0:
            self.direction = 'right'
            pass
        pass
    pass


def main():
    # 首先创建一个窗口 用来显示内容
    screen = pygame.display.set_mode((330, 500), depth=32)
    # 设定一个背景图片
    background = pygame.image.load('./feiji/background.png')
    # 设置一个标题
    pygame.display.set_caption('阶段总结 - 飞机小游戏')
    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./feiji/background.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # 循环次数 -1表示无限循环
    # 创建一个飞机对象
    hero = HeroPlane(screen)
    # 创建一个敌机对象
    enemyplane = Enemy(screen)
    while True:
        screen.blit(background, (0, 0))
        # 显示玩家图片，需要给一个坐标
        hero.display()
        enemyplane.display()  # 显示
        enemyplane.move()  # 敌机移动
        enemyplane.shoot()  # 敌机发射子弹
        # 获取键盘事件
        key_control(hero)
        # 更新显示的内容
        pygame.display.update()
        pygame.time.Clock().tick(20)
    pass


if __name__ == '__main__':
    main()
