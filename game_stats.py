class GameStats():
    """record the statas of game"""
    def __init__(self, ai_settings):
        """initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        self.high_score = 0


    def reset_stats(self):
        """initialize the stats which may change during game"""
        # the left number of ship
        self.ships_left = self.ai_settings.ship_limit

        # the original score
        self.score = 0

        # the original level
        self.level = 1