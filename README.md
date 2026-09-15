# python-practice

Practice problems written alongside CS50P. Every function returns a value and is checked by an automated test file.

## Layout

```
week0/   functions, variables, strings        20 problems   python week0/check.py
week1/   conditionals, and/or/not, modulo     20 problems   python week1/check.py
```

Each folder has a `check.py` that runs every function against known inputs and prints PASS or FAIL with a running score.

## Testing a single function by hand

Use the REPL when you want to try a value the checker doesn't cover, especially boundaries.

```
cd  <the folder the file is in>
python
>>> from <filename without .py> import <function name>
>>> <function name>(<a value>)
>>> exit()
```

Example:

```bash
cd week1
python
```
```
>>> from ranges import letter_grade
>>> letter_grade(80)
'B'
>>> exit()
```

### Rules

- A "module" is just a `.py` file. `No module named 'ranges'` means Python can't see `ranges.py` from where you're standing. `cd` into the right folder.
- Never type the `>>>`. It's the prompt.
- Use `python`, not `python3`, on this machine. That gets 3.12. The system `python3` is 3.9 and doesn't support `match`.
- Import several at once: `from ranges import letter_grade, is_passing`
- If you edit the file while the REPL is open, it won't see the change. `exit()`, start `python`, import again.
- Type the function name alone (no parentheses) to confirm it loaded.

## Workflow

1. Read the problem comment in the file.
2. Write the function.
3. `python weekN/check.py` from the repo root.
4. When it passes, open the REPL and try the edges yourself: 0, negatives, exact boundaries, empty strings.
5. Commit when a file is done.

## Habits

- Pseudocode in a comment before writing code.
- Run the checker before changing something that already passes.
- Four spaces for indentation, everywhere.
- Name variables for what they hold.
