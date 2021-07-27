import pygame

# 游戏的初始化
pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
background = pygame.image.load("./images/background.png")
screen.blit(background, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))

# 可以再所有绘制工作完成后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 游戏循环 -> 意味这游戏的正式开始
while True:

    # 可以指定循环提内部代码的执行频率
    clock.tick(60)

    # 2.修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机位置
    if hero_rect.y + hero_rect.height <= 0:
        hero_rect.y = 700

    # 3.调用blit方法绘制图像
    screen.blit(background, (0, 0))
    screen.blit(hero, hero_rect)

    # 4.调用update方法更新显示
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

pygame.quit()
