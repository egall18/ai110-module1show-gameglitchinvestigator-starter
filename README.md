# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
   1. Game is to guess a hidden number within a limited number of attempts, while using higher/lower hints to guide each next guess.
- [ ] Detail which bugs you found.
   1. Hints were reversed: when the guess was too high, the app said “Go HIGHER,” and when the guess was too low, it said “Go LOWER.”
   2. New Game did not fully reset state, so after a win/loss the app could remain blocked instead of returning to active play.
   3. Secret comparison path was inconsistent because secret handling changed by attempt flow, which made gameplay feel unreliable.
   4. Attempt tracking had off-by-one and flow issues, making remaining-attempt behavior confusing.
   5. Difficulty behavior was inconsistent across rounds, including reset behavior not always matching the selected difficulty context.
   6. Test coverage originally exposed unfinished core logic in logic_utils.py (NotImplementedError), showing the game rules were not fully implemented in the shared module.
- [ ] Explain what fixes you applied.
   1. I fixed hint logic so feedback now matches the guess result:
if the guess is too high, the app says go lower; if too low, it says go higher.

   2. I fixed New Game state reset by resetting all key session values (attempts, secret, status, history, score), so the game no longer stays stuck after a prior win/loss.

   3. I removed inconsistent secret handling during guess evaluation and now compare guesses against the stable session secret value directly.

   4. I implemented the previously unfinished core functions in logic_utils.py (get_range_for_difficulty, parse_guess, check_guess, update_score) so shared logic is complete.

   5. I refactored app.py to import and use logic from logic_utils.py as a single source of truth, reducing duplicated code and mismatch risk.

   6. I added regression and stability tests:

   7. I validated everything with pytest, and the suite now passes (15 passed).


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Open the app and select a difficulty (Easy, Normal, or Hard) from the sidebar. The game now shows the correct range and attempt limit for that difficulty.

2. Expand Developer Debug Info to view the secret number, current attempts, score, and guess history for verification while testing.

3. Enter a guess and click Submit Guess. The app now gives correct hints:
If your guess is too high, it tells you to go lower.
If your guess is too low, it tells you to go higher.

4. Keep guessing until you win or run out of attempts. The attempt counter updates consistently, and score updates based on the current outcome.

5. Click New Game to reset the round. The app now fully resets attempts, status, history, score, and secret number without getting stuck in a won/lost blocked state.

6. Change difficulty and start another round to confirm behavior is stable across modes and ranges.


**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
