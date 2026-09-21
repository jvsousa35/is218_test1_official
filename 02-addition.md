# Issue 2 — Implement and test addition

## Objective

Write your own addition function and three tests. Work on branch `addition`, starting
from your updated `main`. Create this issue in your fork before you start.

## Acceptance checklist

- [ ] `calculator/__init__.py` defines `add(a, b)` and returns the computed sum.
- [ ] `tests/operations/test_add.py` contains all three named tests below.
- [ ] Each test imports/calls the calculator function and asserts the returned value.
- [ ] I have observed an assertion fail during development and corrected the implementation.
- [ ] All three addition tests pass locally.
- [ ] My work is reviewed, committed with the issue number, pushed, merged, and the issue closed.

## Instructions

**Where:** Editor, create these files outside `.venv`:

```text
calculator/__init__.py
tests/operations/test_add.py
```

**Do:** Write `add(a, b)` yourself. It accepts two numbers and returns their sum.
In the test file, import `add` from `calculator`. Write an ordinary pytest test
function for each row. Choose the inputs, call the function, and assert the result.

| Required test name | Inputs | Expected result |
| --- | --- | --- |
| `test_add` | `2, 3` | `5` |
| `test_add_zero` | `7, 0` | `7` |
| `test_add_negative` | `-4, 1` | `-3` |

To see a meaningful failure, begin with a temporary function returning an incorrect
value. Save both files, run your first test, and read the actual/expected values.
An import error or “no tests ran” is a setup problem, not the intended assertion
failure. Then make the function calculate correctly and finish the other tests.
You do not need to commit the temporary incorrect implementation.

**Where:** Terminal, repository root with your project environment selected.

```bash
python -m pytest tests/operations/test_add.py -v
```

**Expect:** `3 passed`. Printing the answer instead of returning it is insufficient.
Returning a fixed result is also insufficient. Do not copy a solution or use AI
completion to write these files.

**If different:** Save your edits and inspect the failing assertion. Check names,
imports, and directory placement using [troubleshooting](../docs/TROUBLESHOOTING.md).

Follow [the task workflow](../docs/WALKTHROUGH.md#4-repeat-for-addition-subtraction-and-delivery)
to commit and merge. The full assessment still fails until subtraction is complete.
