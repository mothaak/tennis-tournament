import pytest
from tennis.set import Set
from tennis.constants import InvalidPlayerError


def test_set_initial_score():
    set_game = Set("player 1", "player 2")
    assert set_game.score() == "0-0, 0-0"


def test_set_win_game():
    set_game = Set("player 1", "player 2")
    for _ in range(4):
        set_game.point_won_by("player 1")
    assert set_game.score() == "1-0"


def test_set_win_by_six_zero():
    set_game = Set("player 1", "player 2")
    for _ in range(6):
        for _ in range(4):
            set_game.point_won_by("player 1")
    assert set_game.score() == "6-0"
    assert set_game.has_winner()


def test_set_seven_five():
    set_game = Set("player 1", "player 2")
    # Get to 5-5
    for _ in range(5):
        for _ in range(4):
            set_game.point_won_by("player 1")
        for _ in range(4):
            set_game.point_won_by("player 2")

    # Win 7-5
    for _ in range(2):
        for _ in range(4):
            set_game.point_won_by("player 1")
    assert set_game.score() == "7-5"
    assert set_game.has_winner()


def test_set_tiebreak_start():
    set_game = Set("player 1", "player 2")
    # Get to 6-6
    for _ in range(6):
        for _ in range(4):
            set_game.point_won_by("player 1")
        for _ in range(4):
            set_game.point_won_by("player 2")

    assert "6-6" in set_game.score()
    set_game.point_won_by("player 1")
    assert "6-6, 1-0" in set_game.score()


def test_set_invalid_player():
    set_game = Set("player 1", "player 2")
    with pytest.raises(InvalidPlayerError):
        set_game.point_won_by("player 3")
