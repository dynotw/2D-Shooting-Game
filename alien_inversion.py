import pygame
import game_functions as gf

from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
from scoreboard import Scoreboard
from alien import Alien
from pygame.sprite import Group

def run_game():
    # 初始化pygame & settings & 一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create sample of Button
    play_button = Button(ai_settings, screen, "Play")

    # set up an example of GameStats
    stats = GameStats(ai_settings)

    # Class Scoreboard installisation and create a score board
    sb = Scoreboard(ai_settings, screen, stats)

    # set up a ship
    ship = Ship(ai_settings, screen)

    # set up an alien
    # alien = Alien(ai_settings, screen)

    # set up a group of bullet
    bullets = Group()

    # set up a group of alien
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
                # bullets.update()
                #
                # # delete the bullets which moving out of screen
                # for bullet in bullets.copy():
                #     if bullet.rect.bottom <=0:
                #         bullets.remove(bullet)
                #
                # # show the left number of bullets, but I think there is no meaning
                # print(len(bullets))


            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

        # # 每次循环时都重绘屏幕
        # screen.fill(ai_settings.bg_color)
        #
        # ship.blitme()
        #
        # # 让最近绘制的屏幕可见
        # pygame.display.flip()

run_game()