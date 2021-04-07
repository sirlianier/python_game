class Settings:
    """"A class to store all setting for example game"""

    def __init__(self):
        """"Initialize the game settings"""
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (238,238,228)
        # ship settings
        self.ship_speed_factor = 0.5