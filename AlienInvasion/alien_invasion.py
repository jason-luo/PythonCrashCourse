import sys
import pygame

from button import Button
from game_stats import GameStats
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()

    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    #  游戏状态
    stats = GameStats(ai_settings)

    # 开始按钮
    play_button = Button(ai_settings, screen, "Play")

    # 飞船
    ship = Ship(ai_settings, screen)

    # 飞船子弹
    bullets = Group()

    # 外星人
    aliens = Group()

    # 外星舰队
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        # 键盘鼠标事件
        gf.check_event(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


# 程序入口
run_game()
