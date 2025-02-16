from typing import Optional
from .constants import (
    POINTS_TO_WIN_TIEBREAK, MIN_POINT_DIFFERENCE,
    GAME_SCORE_FORMAT, PlayerName, InvalidPlayerError,
    INVALID_PLAYER_ERROR, INITIAL_POINTS
)


class TieBreak:
    def __init__(self, player_one: PlayerName, player_two: PlayerName) -> None:
        self.player_one = player_one
        self.player_two = player_two
        self.player_one_points = INITIAL_POINTS
        self.player_two_points = INITIAL_POINTS

    def point_won_by(self, player_name: PlayerName) -> None:
        if player_name not in [self.player_one, self.player_two]:
            raise InvalidPlayerError(INVALID_PLAYER_ERROR.format(player_name))
        if player_name == self.player_one:
            self.player_one_points += 1
        else:
            self.player_two_points += 1

    def score(self) -> str:
        return GAME_SCORE_FORMAT.format(
            self.player_one_points,
            self.player_two_points
        )

    def has_winner(self) -> bool:
        p1_points = self.player_one_points
        p2_points = self.player_two_points
        return (
            (p1_points >= POINTS_TO_WIN_TIEBREAK and
             p1_points >= p2_points + MIN_POINT_DIFFERENCE) or
            (p2_points >= POINTS_TO_WIN_TIEBREAK and
             p2_points >= p1_points + MIN_POINT_DIFFERENCE)
        )

    def winner(self) -> Optional[PlayerName]:
        if not self.has_winner():
            return None
        return (
            self.player_one
            if self.player_one_points > self.player_two_points
            else self.player_two
        )
