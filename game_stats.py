class GameStats():
    """Game statistics"""
    def __init__(self, game_settings):
        """Inittialize statistics"""
        self.game_settings = game_settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """initialize statistics, change during the game"""
        self.ships_left = self.game_settings.ship_limit