import pytest
from tennis.game import Game
from tennis.constants import DEUCE, ADVANTAGE, InvalidPlayerError


def test_game_initial_score():
    game = Game("player 1", "player 2")
    assert game.score() == "0-0"


def test_game_basic_scoring():
    game = Game("player 1", "player 2")
    game.point_won_by("player 1")
    assert game.score() == "15-0"

    game.point_won_by("player 2")
    assert game.score() == "15-15"

    game.point_won_by("player 1")
    game.point_won_by("player 1")
    assert game.score() == "40-15"


def test_game_deuce():
    game = Game("player 1", "player 2")
    points = ["player 1", "player 1", "player 1",
              "player 2", "player 2", "player 2"]
    for player in points:
        game.point_won_by(player)
    assert game.score() == DEUCE


def test_game_advantage():
    game = Game("player 1", "player 2")
    points = ["player 1", "player 1", "player 1",
              "player 2", "player 2", "player 2"]
    for player in points:
        game.point_won_by(player)

    game.point_won_by("player 1")
    assert game.score() == f"{ADVANTAGE} player 1"


def test_game_win_straight():
    game = Game("player 1", "player 2")
    for _ in range(4):
        game.point_won_by("player 1")
    assert game.has_winner()
    assert game.winner() == "player 1"


def test_game_win_from_advantage():
    game = Game("player 1", "player 2")
    points = ["player 1", "player 1", "player 1",
              "player 2", "player 2", "player 2",
              "player 1", "player 1"]
    for player in points:
        game.point_won_by(player)
    assert game.has_winner()
    assert game.winner() == "player 1"


def test_game_invalid_player():
    game = Game("player 1", "player 2")
    with pytest.raises(InvalidPlayerError):
        game.point_won_by("player 3")
