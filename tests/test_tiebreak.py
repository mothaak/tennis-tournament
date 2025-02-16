import pytest
from tennis.tiebreak import TieBreak
from tennis.constants import InvalidPlayerError


def test_tiebreak_initial_score():
    tiebreak = TieBreak("player 1", "player 2")
    assert tiebreak.score() == "0-0"


def test_tiebreak_basic_scoring():
    tiebreak = TieBreak("player 1", "player 2")
    tiebreak.point_won_by("player 1")
    assert tiebreak.score() == "1-0"

    tiebreak.point_won_by("player 2")
    assert tiebreak.score() == "1-1"


def test_tiebreak_win_by_two():
    tiebreak = TieBreak("player 1", "player 2")
    # Get to 6-6
    for _ in range(6):
        tiebreak.point_won_by("player 1")
        tiebreak.point_won_by("player 2")

    # Win by 2
    tiebreak.point_won_by("player 1")
    tiebreak.point_won_by("player 1")
    assert tiebreak.has_winner()
    assert tiebreak.winner() == "player 1"


def test_tiebreak_minimum_points():
    tiebreak = TieBreak("player 1", "player 2")
    for _ in range(7):
        tiebreak.point_won_by("player 1")
    assert tiebreak.has_winner()
    assert tiebreak.winner() == "player 1"


def test_tiebreak_invalid_player():
    tiebreak = TieBreak("player 1", "player 2")
    with pytest.raises(InvalidPlayerError):
        tiebreak.point_won_by("player 3")
