import pygame

# 游戏的初始化
pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
background = pygame.image.load("./images/background.png")
screen.blit(background, (0, 0))
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))

# 可以再所有绘制工作完成后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环 -> 意味这游戏的正式开始
i = 0
while True:

    # 可以指定循环提内部代码的执行频率
    clock.tick(60)
    
    print(i)
    i += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

pygame.quit()
