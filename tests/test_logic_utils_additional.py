from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_get_range_for_difficulty_values():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_get_range_for_difficulty_default_for_unknown():
    assert get_range_for_difficulty("Impossible") == (1, 100)


def test_parse_guess_none_and_empty():
    ok, guess, err = parse_guess(None)
    assert ok is False
    assert guess is None
    assert err == "Enter a guess."

    ok, guess, err = parse_guess("")
    assert ok is False
    assert guess is None
    assert err == "Enter a guess."

    ok, guess, err = parse_guess("   ")
    assert ok is False
    assert guess is None
    assert err == "Enter a guess."


def test_parse_guess_numeric_formats():
    ok, guess, err = parse_guess("42")
    assert ok is True
    assert guess == 42
    assert err is None

    ok, guess, err = parse_guess("  17 ")
    assert ok is True
    assert guess == 17
    assert err is None

    ok, guess, err = parse_guess("42.9")
    assert ok is True
    assert guess == 42
    assert err is None


def test_parse_guess_invalid_text():
    ok, guess, err = parse_guess("abc")
    assert ok is False
    assert guess is None
    assert err == "That is not a number."


def test_check_guess_outcomes_and_messages():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_check_guess_type_mismatch_fallback():
    outcome, _ = check_guess(5, "5")
    assert outcome == "Win"


def test_update_score_win_minimum_points_floor():
    score = update_score(current_score=0, outcome="Win", attempt_number=20)
    assert score == 10


def test_update_score_too_high_even_and_odd_attempts():
    score_even = update_score(current_score=10, outcome="Too High", attempt_number=2)
    score_odd = update_score(current_score=10, outcome="Too High", attempt_number=3)
    assert score_even == 15
    assert score_odd == 5


def test_update_score_too_low_and_unknown_outcome():
    score_low = update_score(current_score=10, outcome="Too Low", attempt_number=1)
    score_unknown = update_score(current_score=10, outcome="Unknown", attempt_number=1)
    assert score_low == 5
    assert score_unknown == 10
