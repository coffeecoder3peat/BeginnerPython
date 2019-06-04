class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        #Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score should never be reset
        self.high_score = self.get_high_score()

    def reset_stats(self):
        """Initialize statistics that can change throughout the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def get_high_score(self):
        """Gets the high score from a file."""
        with open('pythonCrashCourse\ALien_Invasion\high_score.txt') as file_object:
            high_score = file_object.read()
        high_score_int = int(high_score)

        return high_score_int