class Player:
    def __init__(self, name, account = 5000, played_games = 0, won_games = 0):
        self.name = name
        self.account = 5000
        self.played_games = 0
        self.won_games = 0

    @classmethod
    def find_by_name(self, name):
        pass