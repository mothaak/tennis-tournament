import pytest
from tennis import Match
from tennis.constants import InvalidPlayerError


def test_initial_score():
    match = Match("player 1", "player 2")
    assert match.score() == "0-0, 0-0"


def test_basic_points():
    match = Match("player 1", "player 2")
    match.point_won_by("player 1")
    assert match.score() == "0-0, 15-0"

    match.point_won_by("player 2")
    assert match.score() == "0-0, 15-15"

    match.point_won_by("player 1")
    match.point_won_by("player 1")
    assert match.score() == "0-0, 40-15"


def test_deuce_scenarios():
    match = Match("player 1", "player 2")
    # Get to deuce
    points = ["player 1", "player 1", "player 1",
              "player 2", "player 2", "player 2"]
    for player in points:
        match.point_won_by(player)
    assert match.score() == "0-0, Deuce"

    # Test advantage
    match.point_won_by("player 1")
    assert match.score() == "0-0, Advantage player 1"

    # Back to deuce
    match.point_won_by("player 2")
    assert match.score() == "0-0, Deuce"


def test_winning_a_game():
    match = Match("player 1", "player 2")
    # Win by straight points
    for _ in range(4):
        match.point_won_by("player 1")
    assert match.score() == "1-0"


def test_winning_from_advantage():
    match = Match("player 1", "player 2")
    # Get to deuce
    points = ["player 1", "player 1", "player 1",
              "player 2", "player 2", "player 2"]
    for player in points:
        match.point_won_by(player)
    # Win from advantage
    match.point_won_by("player 1")
    match.point_won_by("player 1")
    assert match.score() == "1-0"


def test_set_scoring():
    match = Match("player 1", "player 2")
    # Win 6 games straight
    for _ in range(6):
        for _ in range(4):
            match.point_won_by("player 1")
    assert match.score() == "6-0"


def test_set_with_close_games():
    match = Match("player 1", "player 2")
    # Get to 5-5
    for _ in range(5):
        for _ in range(4):
            match.point_won_by("player 1")
        for _ in range(4):
            match.point_won_by("player 2")

    # Win two more games for 7-5
    for _ in range(2):
        for _ in range(4):
            match.point_won_by("player 1")
    assert match.score() == "7-5"


def test_tiebreak_scenario():
    match = Match("player 1", "player 2")
    # Get to 6-6
    for _ in range(6):
        for _ in range(4):
            match.point_won_by("player 1")
        for _ in range(4):
            match.point_won_by("player 2")
    assert "6-6" in match.score()

    # Test tiebreak scoring
    match.point_won_by("player 1")
    assert "6-6, 1-0" in match.score()

    # Win tiebreak
    for _ in range(6):
        match.point_won_by("player 1")
    assert match.score() == "7-6"


def test_tiebreak_close_finish():
    match = Match("player 1", "player 2")
    # Get to 6-6
    for _ in range(6):
        for _ in range(4):
            match.point_won_by("player 1")
        for _ in range(4):
            match.point_won_by("player 2")

    # Get to 6-6 in tiebreak
    for _ in range(6):
        match.point_won_by("player 1")
        match.point_won_by("player 2")

    # Win by 2 in tiebreak
    match.point_won_by("player 1")
    match.point_won_by("player 1")
    assert match.score() == "7-6"


def test_six_five_scenario():
    match = Match("player 1", "player 2")
    # Get to 5-5
    for _ in range(5):
        for _ in range(4):
            match.point_won_by("player 1")
        for _ in range(4):
            match.point_won_by("player 2")

    # Get to 6-5
    for _ in range(4):
        match.point_won_by("player 1")
    assert match.score() == "6-5"

    # Win 7-5
    for _ in range(4):
        match.point_won_by("player 1")
    assert match.score() == "7-5"


def test_advantage_alternating():
    match = Match("player 1", "player 2")
    # Get to deuce
    points = ["player 1", "player 1", "player 1",
              "player 2", "player 2", "player 2"]
    for player in points:
        match.point_won_by(player)

    # Test alternating advantages
    match.point_won_by("player 1")
    assert match.score() == "0-0, Advantage player 1"
    match.point_won_by("player 2")
    assert match.score() == "0-0, Deuce"
    match.point_won_by("player 2")
    assert match.score() == "0-0, Advantage player 2"


def test_tiebreak_minimum_points():
    match = Match("player 1", "player 2")
    # Get to 6-6
    for _ in range(6):
        for _ in range(4):
            match.point_won_by("player 1")
        for _ in range(4):
            match.point_won_by("player 2")

    # Test winning with exactly 7 points
    for _ in range(7):
        match.point_won_by("player 1")
    assert match.score() == "7-6"


def test_losing_at_six_five():
    match = Match("player 1", "player 2")
    # Get to 5-5
    for _ in range(5):
        for _ in range(4):
            match.point_won_by("player 1")
        for _ in range(4):
            match.point_won_by("player 2")

    # Get to 6-5
    for _ in range(4):
        match.point_won_by("player 1")

    # Player 2 wins to force tiebreak
    for _ in range(4):
        match.point_won_by("player 2")
    assert "6-6" in match.score()


def test_match_integration_deuce_advantage():
    match = Match("player 1", "player 2")
    # Get to deuce
    points = ["player 1", "player 1", "player 1",
              "player 2", "player 2", "player 2"]
    for player in points:
        match.point_won_by(player)
    assert match.score() == "0-0, Deuce"

    # Test alternating advantages
    match.point_won_by("player 1")
    assert match.score() == "0-0, Advantage player 1"
    match.point_won_by("player 2")
    assert match.score() == "0-0, Deuce"
    match.point_won_by("player 2")
    assert match.score() == "0-0, Advantage player 2"


def test_match_integration_tiebreak():
    match = Match("player 1", "player 2")
    # Get to 6-6
    for _ in range(6):
        for _ in range(4):
            match.point_won_by("player 1")
        for _ in range(4):
            match.point_won_by("player 2")

    assert "6-6" in match.score()

    # Win tiebreak
    for _ in range(7):
        match.point_won_by("player 1")
    assert match.score() == "7-6"


def test_match_invalid_player():
    match = Match("player 1", "player 2")
    with pytest.raises(InvalidPlayerError):
        match.point_won_by("player 3")
