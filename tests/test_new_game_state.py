from logic_utils import build_new_game_state


def test_new_game_resets_to_playing_state():
    state = build_new_game_state(1, 20, randint_fn=lambda lo, hi: 7)

    assert state["status"] == "playing"
    assert state["attempts"] == 0
    assert state["history"] == []
    assert state["score"] == 0
    assert state["secret"] == 7


def test_new_game_secret_respects_difficulty_range():
    state = build_new_game_state(1, 20, randint_fn=lambda lo, hi: hi)

    assert 1 <= state["secret"] <= 20
