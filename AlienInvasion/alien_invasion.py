import sys
import pygame

from alien import Alien
from button import Button
from game_stats import GameStats
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化
    pygame.init()

    ai_settings = Settings()
    # 设置分辨率
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # 设置标题
    pygame.display.set_caption("Alien Invasion")

    # 创建开始按钮
    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)

    # 创建飞船
    ship = Ship(ai_settings, screen)

    bullets = Group()

    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_event(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


# 程序入口
run_game()
