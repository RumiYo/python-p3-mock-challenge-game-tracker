class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter 
    def title(self, title):
        if not hasattr(self, 'title'):
            if isinstance(title, str) and len(title):
                self._title = title
            else:
                raise TypeError(
                    "Title must be a non-empty string"
                )
        else:
            raise TypeError(
                "Title is an immutable string"
            )

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        # player_list = []
        # for result in Result.all:
        #     if result.game == self:
        #         if result.player not in player_list:
        #             player_list.append(result.player)
        # return player_list

        return list(set([result.player for result in Result.all if result.game == self]))

    def average_score(self, player):
        player_scores = []
        game_results = Game.results(self)
        for result in game_results:
            if result.player == player:
                player_scores.append(result.score)
        return sum(player_scores)/len(player_scores)

class Player:

    all =[]

    def __init__(self, username):
        self.username = username
        if self not in Player.all:
            Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str):
            if len(username) >= 2 and len(username) <= 16:
                self._username = username
            else:
                raise TypeError(
                    "username is between characters 2 and 16 characters long"
                )
        else:
            raise TypeError(
                "username is of type str and can change"
            )

    def results(self):
        return [result for result in Result.all if result.player ==self]

    def games_played(self):
        return list(set([result.game for result in Result.all if result.player == self]))

    def played_game(self, game):
        games = Player.games_played(self)
        return game in games


    def num_times_played(self, game):
        played_amount = 0
        all_game_results = Player.results(self)
        for result in all_game_results:
            if result.game == game:
                played_amount += 1
        return played_amount

    @classmethod
    def highest_scored(cls, game):
        game_plays = []
        for item in Result.all:
            if item.game == game:
                game_plays.append(item)
        
        if len(game_plays) == 0: 
            return None
        else:
            highest_score = game_plays[0]
            for item in game_plays:
                if item.score > highest_score.score:
                    highest_score = item
            return highest_score.player

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not hasattr(self, 'score'):
            if isinstance(score, int):
                if score >=1 and score <=5000: 
                    self._score = score
            else:
                raise TypeError(
                    "score is integer"
                )
        else:
            raise TypeError(
                "result score is an immutable integer"
            )

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if not isinstance(player, Player):
            raise TypeError(
                "player must be an instance of Player class"
            )
        self._player = player

    @property
    def game(self):
        return self._game 

    @game.setter
    def game(self, game):
        if not isinstance(game, Game):
            raise TypeError(
                "game must be an instance of Game class"
            )
        self._game = game
