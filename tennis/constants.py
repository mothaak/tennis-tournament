"""Constants used in tennis scoring system."""

from typing import NewType, Literal


class InvalidPlayerError(Exception):
    pass


# Type definitions
PlayerName = NewType('PlayerName', str)
GameScore = Literal["0", "15", "30", "40", "Deuce", "Advantage"]

# Game scoring
LOVE: GameScore = "0"
FIFTEEN: GameScore = "15"
THIRTY: GameScore = "30"
FORTY: GameScore = "40"
DEUCE: GameScore = "Deuce"
ADVANTAGE: str = "Advantage"

# Points needed
POINTS_TO_WIN_GAME: int = 4
POINTS_TO_WIN_TIEBREAK: int = 7
GAMES_TO_WIN_SET: int = 6
GAMES_FOR_TIEBREAK: int = 6
MIN_POINTS_FOR_DEUCE: int = 3

# Score formats
GAME_SCORE_FORMAT: str = "{}-{}"
SET_SCORE_FORMAT: str = "{}-{}"
ADVANTAGE_SCORE_FORMAT: str = "Advantage {}"
GAME_AND_SET_FORMAT: str = "{}, {}"

# Point differences
MIN_POINT_DIFFERENCE: int = 2
MIN_GAME_DIFFERENCE: int = 2

# Initial values
INITIAL_POINTS: int = 0
INITIAL_GAMES: int = 0

# Error messages
INVALID_PLAYER_ERROR: str = "Invalid player: {}"
