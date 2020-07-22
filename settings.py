class Settings():
    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width=1000
        self.screen_height=600
        # setting background color
        self.bg_color=(230,230,230)

        # set up the parameter of bullet
        # self.bullet_speed_factor = 0.8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3

        # set up the speed of alien
        # self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1 represents right
        self.fleet_direction = 1

        # set up the parameter of ship
        # self.ship_speed_factor = 1.0
        self.ship_limit = 3

        # the speedup rate of game
        self.speedup_scale = 1.1

        # the points of alien raising rate
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize the dynamic settings"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet direction: '1' represents right
        self.fleet_direction = 1

        # score of each alien
        self.alien_points = 50


    def increase_speed(self):
        """speedup settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
