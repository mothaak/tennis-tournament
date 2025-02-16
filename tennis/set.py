from .game import Game
from .tiebreak import TieBreak
from .constants import (
    GAMES_TO_WIN_SET, MIN_GAME_DIFFERENCE,
    GAMES_FOR_TIEBREAK, SET_SCORE_FORMAT,
    GAME_AND_SET_FORMAT, PlayerName,
    InvalidPlayerError, INVALID_PLAYER_ERROR,
    INITIAL_GAMES
)


class Set:
    def __init__(self, player_one: PlayerName, player_two: PlayerName) -> None:
        self.player_one = player_one
        self.player_two = player_two
        self.player_one_games = INITIAL_GAMES
        self.player_two_games = INITIAL_GAMES
        self.current_game = Game(player_one, player_two)
        self.tiebreak = None

    def point_won_by(self, player_name: PlayerName) -> None:
        if player_name not in [self.player_one, self.player_two]:
            raise InvalidPlayerError(INVALID_PLAYER_ERROR.format(player_name))

        if self.tiebreak:
            self.tiebreak.point_won_by(player_name)
            if self.tiebreak.has_winner():
                self.handle_tiebreak_winner(self.tiebreak.winner())
            return

        self.current_game.point_won_by(player_name)
        if self.current_game.has_winner():
            self.handle_game_winner(self.current_game.winner())

    def handle_game_winner(self, winner: PlayerName) -> None:
        if winner == self.player_one:
            self.player_one_games += 1
        else:
            self.player_two_games += 1

        if not self.has_winner() and self.should_start_tiebreak():
            self.tiebreak = TieBreak(self.player_one, self.player_two)
        else:
            self.current_game = Game(self.player_one, self.player_two)

    def handle_tiebreak_winner(self, winner: PlayerName) -> None:
        if winner == self.player_one:
            self.player_one_games += 1
        else:
            self.player_two_games += 1

    def score(self) -> str:
        set_score = SET_SCORE_FORMAT.format(
            self.player_one_games,
            self.player_two_games
        )

        if self.has_winner():
            return set_score

        if self.tiebreak:
            tiebreak_score = self.tiebreak.score()
            if tiebreak_score and not self.tiebreak.has_winner():
                return GAME_AND_SET_FORMAT.format(
                    set_score,
                    tiebreak_score
                )
            return set_score

        game_score = self.current_game.score()
        if game_score is None:
            return set_score

        if self.current_game.has_winner():
            return set_score

        initial_games = (
            self.player_one_games == INITIAL_GAMES and
            self.player_two_games == INITIAL_GAMES
        )
        if initial_games:
            return GAME_AND_SET_FORMAT.format(set_score, game_score)

        return set_score

    def has_winner(self) -> bool:
        p1_games = self.player_one_games
        p2_games = self.player_two_games
        return (
            (p1_games >= GAMES_TO_WIN_SET and
             p1_games >= p2_games + MIN_GAME_DIFFERENCE) or
            (p2_games >= GAMES_TO_WIN_SET and
             p2_games >= p1_games + MIN_GAME_DIFFERENCE) or
            p1_games == 7 or p2_games == 7
        )

    def should_start_tiebreak(self) -> bool:
        return (self.player_one_games == GAMES_FOR_TIEBREAK and
                self.player_two_games == GAMES_FOR_TIEBREAK)
