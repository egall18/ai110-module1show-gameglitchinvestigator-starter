# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the agent to debug and stabilize the Streamlit guessing game end-to-end. The goal was to verify reported gameplay bugs (wrong hints, blocked New Game state, inconsistent guess behavior), implement fixes, refactor shared logic into `logic_utils.py`, and add tests until the suite passed.

**What did the agent do?**

1. Diagnosed environment and dependency issues, then used a local virtual environment with Python 3.13.
2. Inspected `app.py`, `logic_utils.py`, and existing tests to confirm bug sources.
3. Implemented New Game reset logic (`status`, `attempts`, `history`, `score`, `secret`) with a helper in `logic_utils.py`.
4. Fixed gameplay logic issues in `check_guess` and removed inconsistent secret-handling behavior in `app.py`.
5. Implemented missing functions in `logic_utils.py` (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`).
6. Refactored `app.py` to import shared logic from `logic_utils.py` so behavior and tests use one source of truth.
7. Added and updated tests in `tests/test_game_logic.py`, `tests/test_new_game_state.py`, and `tests/test_logic_utils_additional.py`.
8. Ran pytest repeatedly and verified final passing result (`15 passed`).

**What did you have to verify or fix manually?**

I manually verified behavior in the app UI (especially New Game flow and hint direction) because passing tests alone do not guarantee good gameplay UX. I also confirmed terminal command usage (`python -m pytest`) to avoid interpreter/path mismatches that happened with plain `pytest`.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| New Game after win/loss should not stay blocked | "Add test coverage for this issue: If player was won/lost, pressing New Game may keep game blocked." | Added tests for `build_new_game_state` to assert `status == "playing"`, reset attempts/history/score, and in-range secret generation. | Yes | This directly validates the state-reset bug path and prevents regressions. |
| Input parsing edge cases | "Add more test coverage to ensure stability of logic code." | Added tests for `parse_guess(None)`, empty string, whitespace, integer text, decimal text, and invalid text. | Yes | Input handling is a common failure source in UI apps; these tests harden validation behavior. |
| Guess/scoring behavior consistency | "Add more tests for check_guess and update_score edge cases." | Added tests for win/high/low outcomes, hint message direction, mixed-type fallback, score floor on late win, and too-high even/odd scoring differences. | Yes | These tests cover core game rules and verify bug fixes for hint correctness and score logic. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
