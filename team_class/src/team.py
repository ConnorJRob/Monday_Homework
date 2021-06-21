import pdb

class Team:
    def __init__(self, Name, Players, Coach):
        self.name = Name
        self.players = Players
        self.coach = Coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, search_player):
        # pdb.set_trace()
        player_found = False
        for player in self.players:
            if player == search_player:
                player_found = True
        return player_found

    def play_game(self, win_lose):
        if win_lose == True:
            self.points += 3
