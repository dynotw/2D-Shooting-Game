import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """initialize the property of button"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set th size and other property of button
        self.width, self.height = 200, 50
        self.button_color = (0, 250, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # create button's rect and make it center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the tag of button only need to be created once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """make msg an image and make it center"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """paint a colorful button and write some text"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)