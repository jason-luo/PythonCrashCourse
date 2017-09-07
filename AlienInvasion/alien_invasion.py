import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化
    pygame.init()

    ai_settings = Settings()
    # 设置分辨率
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # 设置标题
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(ai_settings, screen)

    while True:
        gf.check_event(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

# 程序入口
run_game()
