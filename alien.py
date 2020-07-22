import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # 继承Sprite类

    def __init__(self, ai_settings, screen):
        # 初始化外星人并设定起始位置
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像， 并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # every alien will appear on the left-top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the position of aliens
        self.x = float(self.rect.x)

    def blitme(self):
        # create alien on the appointed position
        # screen.blit(x,(ix,iy)) is a function that load x 'most is an image' into the position (ix,iy)
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """if alien is on the margin of the screen, it will return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True

        elif self.rect.left < 0:
            return True

    def update(self):
        """let alien move right or left"""
        self.x +=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        # ai_settngs is the parameter of Class Alien and is an example of Class Settings (in main application)
        self.rect.x = self.x


