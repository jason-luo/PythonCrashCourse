import sys
import pygame


def check_event():
    """获取并处理感兴趣的事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像并切换到新屏幕"""
    # 填充屏幕背景色
    screen.fill(ai_settings.bg_color)
    # 显示飞船
    ship.blitme()

    pygame.display.flip()
