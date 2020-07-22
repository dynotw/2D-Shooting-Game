import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super(Ship,self).__init__()
        self.screen=screen
        self.ai_settings= ai_settings

        # 加载飞船图像并获取其外接矩形
        # 以self为前缀的变量可供类中的所有方法引用
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 默认没有KEYDOWN事件时，moving action 不被激发
        self.moving_right = False
        self.moving_left = False

        # the center aims to store the float part
        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """make the ship in central bottom of screen"""
        self.center = self.screen_rect.centerx