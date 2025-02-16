"""
Tennis scoring system implementation following official rules.

This module implements a tennis scoring system with support for:
- Game scoring (0, 15, 30, 40, Deuce, Advantage)
- Set scoring (6 games with 2-game lead)
- Tiebreak scoring

Example:
    match = Match("player 1", "player 2")
    match.point_won_by("player 1")
    match.score()  # Returns "0-0, 15-0"
"""

from .set import Set
from .constants import PlayerName, InvalidPlayerError, INVALID_PLAYER_ERROR


class Match:
    def __init__(self, player_one: PlayerName, player_two: PlayerName) -> None:
        self.player_one = player_one
        self.player_two = player_two
        self.current_set = Set(player_one, player_two)

    def point_won_by(self, player_name: PlayerName) -> None:
        """
        Record a point won by a player.

        Args:
            player_name: Name of the player who won the point

        Raises:
            InvalidPlayerError: If player_name is not a valid player
        """
        if player_name not in [self.player_one, self.player_two]:
            raise InvalidPlayerError(INVALID_PLAYER_ERROR.format(player_name))
        self.current_set.point_won_by(player_name)

    def score(self) -> str:
        """
        Get the current score.

        Returns:
            str: Current score in tennis format (e.g., "0-0, 15-0")
        """
        return self.current_set.score()
