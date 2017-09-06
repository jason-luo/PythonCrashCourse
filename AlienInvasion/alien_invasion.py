import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    # 初始化
    pygame.init()

    ai_settings = Settings()
    # 设置分辨率
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # 设置标题
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(screen)

    while True:
        # 获取并处理感兴趣的事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 填充屏幕背景色
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让绘制的屏幕可见
        pygame.display.flip()


# 程序入口
run_game()
