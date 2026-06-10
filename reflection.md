# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  New game does not reset status to playing.
   1. If player was won/lost, pressing New Game may keep game blocked.
  Attempt counter starts at 1, creating off-by-one behavior.
   2. Players lose one effective attempt immediately and the UI count can feel wrong.
  Difficulty attempt limits do not match expected values.
   3. New game ignores difficulty range and always picks 1 to 100.
  This breaks consistency for Easy and Hard modes after reset.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 60| "Too High" hint| "Too Low" hint shown| none|
| select normal and guess 80 -> select new game| should have 8 attempts left and a hint| game over start new game and cant start new game| none|
| select easy, normal, and hard and view difficlty range 1-100| different ranges per level of difficulty| same difficulty level on all three| none|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  1. i used claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  1. When analzying the UI and discovering glitches of my own, i used AI to verify if these issues i noticed are also true in our code logic as well, i gave it specific details to the issue i noticed then i asked it to check by selecting the specific file. I then asked it what it suggested the fix to be and to also create tests coverage or fix tests related to this issue.
  2. Ex: i asked it to look into this issue: If player was won/lost, pressing New Game may keep game blocked. I asked it to run test + add test coverage then if test failed to then suggest a code change. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  1. Giving AI no details or files to use gives ambiguous answers.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  1. By running test + adding test and asking AI to run through scenarios where a feature might fail. Also testing UI.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  1. check_guess test failed, the function raised NotImplementedError, it failed during execution. This meant it failed during unfinished core logic not just samll edge cases. It showed that the core logic was incomplete.
- Did AI help you design or understand any tests? How?
  1. Yes, i asked AI to help me create a .md file to understand failing tests and why it is failing. I asked it to also suggest code changes and understand why these changes are being implemented and to add test coverage.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  1. In Streamlit, every time you click a button or change an input, the whole script runs again from top to bottom. If you store values in normal variables, they reset on each rerun, so your app can “forget” things. st.session_state is like a memory box for that user session, so values like score, attempts, or secret number persist between reruns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  1. What i'd reuse is giving AI a very specific debugging prompt with context: the exact bug, expected behavior, relevant file names, and a request for a test case first. That made the AI responses much more useful and less generic. It also helped me verify fixes with pytest instead of guessing from UI behavior alone. I’d keep this workflow: reproduce bug, ask AI with precise context, add test, apply fix, rerun tests.
- What is one thing you would do differently next time you work with AI on a coding task?
  1. I would ask AI to propose a short test plan before any code changes. That would help me validate assumptions early and catch mismatches between expected behavior and actual logic faster. I’d still use AI for fixes, but I’d require test cases first so I can verify each change immediately.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  1. It is very important to understand and judge the outcome of AI responses. AI can be very useful when providing enough context.
