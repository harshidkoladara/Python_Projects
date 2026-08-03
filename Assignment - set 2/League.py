# class League
class League:
    # Games and Teams array to store all the Games and all the teams
    games = []
    teams = []

    # Add team to the league
    @staticmethod
    def add_team(team):
        League.teams.append(team)

    # remove team from the league
    @staticmethod
    def remove_team(team):
        League.teams.remove(team)

    # Show all the details
    @staticmethod
    def __str__():
        for i, team in enumerate(League.teams):
            print(f"{i+1}) Team: {team.name}\n\tPlayers:")
            for j, player in enumerate(team.players):
                print(f"\t\t{j+1}). Name: {player.name}")
            print(f"\tTotal Players: {len(team.players)}\n\tPlayed Games:")
            for j, game in enumerate(team.games):
                print(f"\t\t{j+1}). Game: {game.name}")
            print(f"\tPoints: {team.points}")
            print('\n')

# class Team
class Team:
    # Team constructor to initialize team object
    def __init__(self, name):
        self.name = name
        self.games = []
        self.points = 0
        self.players = []
        League.teams.append(self)

    # Add player
    def add_player(self, player):
        self.players.append(player)

    # Remove Player
    def remove_player(self, player):
        self.players.remove(player)

    # Palyed Games by the pertuculer team
    def game_played(self, game, won):
        self.games.append(game)
        if won:
            self.points += game.win_points


# class Game
class Game:
    # initializing Game Object
    def __init__(self, name, points):
        self.name = name
        self.win_points = points
        League.games.append(self)

# class Player
class Player:
    def __init__(self, name):
        self.name = name
