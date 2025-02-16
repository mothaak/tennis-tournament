"""
Implements tennis game scoring rules.

A game is won by the first player to have won at least 4 points in total and
at least 2 points more than the opponent.
"""

from typing import Optional
from .constants import (
    LOVE, FIFTEEN, THIRTY, FORTY, DEUCE,
    POINTS_TO_WIN_GAME, MIN_POINT_DIFFERENCE,
    GAME_SCORE_FORMAT, ADVANTAGE_SCORE_FORMAT,
    MIN_POINTS_FOR_DEUCE, PlayerName, GameScore,
    InvalidPlayerError, INVALID_PLAYER_ERROR,
    INITIAL_POINTS
)


class Game:
    POINTS_LOOKUP: dict[int, GameScore] = {
        0: LOVE,
        1: FIFTEEN,
        2: THIRTY,
        3: FORTY
    }

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

    def score(self) -> Optional[str]:
        if self.has_winner():
            return None

        if self.is_deuce():
            return DEUCE

        if self.has_advantage():
            leader = (
                self.player_one
                if self.player_one_points > self.player_two_points
                else self.player_two
            )
            return ADVANTAGE_SCORE_FORMAT.format(leader)

        return GAME_SCORE_FORMAT.format(
            self.POINTS_LOOKUP[min(self.player_one_points, 3)],
            self.POINTS_LOOKUP[min(self.player_two_points, 3)]
        )

    def has_winner(self) -> bool:
        return (
            self._has_winning_points(
                self.player_one_points,
                self.player_two_points
            ) or
            self._has_winning_points(
                self.player_two_points,
                self.player_one_points
            )
        )

    def _has_winning_points(self, points: int, opponent_points: int) -> bool:
        return (points >= POINTS_TO_WIN_GAME and
                points >= opponent_points + MIN_POINT_DIFFERENCE)

    def winner(self) -> Optional[PlayerName]:
        if not self.has_winner():
            return None
        return (
            self.player_one
            if self.player_one_points > self.player_two_points
            else self.player_two
        )

    def is_deuce(self):
        return (self.player_one_points >= MIN_POINTS_FOR_DEUCE and
                self.player_two_points >= MIN_POINTS_FOR_DEUCE and
                self.player_one_points == self.player_two_points)

    def has_advantage(self):
        return (self.player_one_points >= MIN_POINTS_FOR_DEUCE and
                self.player_two_points >= MIN_POINTS_FOR_DEUCE and
                abs(self.player_one_points - self.player_two_points) == 1)
