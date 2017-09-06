import sys
import pygame


def run_game():
    # 初始化
    pygame.init()
    # 设置分辨率
    screen = pygame.display.set_mode((1200, 800))

    # 设置标题
    pygame.display.set_caption("Alien Invasion")

    while True:
        # 获取并处理感兴趣的事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 让绘制的屏幕可见
        pygame.display.flip()


# 程序入口
run_game()
