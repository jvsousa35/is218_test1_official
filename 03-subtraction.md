# Issue 3 — Implement and test subtraction

## Objective

Extend the calculator while preserving addition. Work on branch `subtraction`,
starting from updated `main`, and reference your subtraction issue number.

## Acceptance checklist

- [ ] `subtract(a, b)` returns the first argument minus the second.
- [ ] Addition and its tests still work.
- [ ] The three named subtraction tests below call the function and assert its result.
- [ ] All six student tests pass without skips or expected failures.
- [ ] The supplied acceptance checks pass too.
- [ ] My work is reviewed, committed, pushed, merged, and the issue closed.

## Instructions

**Where:** Editor, `calculator/__init__.py` and a new
`tests/operations/test_subtract.py`.

**Do:** Write `subtract(a, b)` yourself, keeping your addition function. Import
`subtract` from `calculator` in the new test file and write these tests:

| Required test name | Inputs | Expected result |
| --- | --- | --- |
| `test_subtract` | `5, 3` | `2` |
| `test_subtract_negative_result` | `3, 5` | `-2` |
| `test_subtract_zero` | `7, 0` | `7` |

**Where:** Terminal, root, using the project environment.

```bash
python -m pytest tests/operations/test_subtract.py -v
python -m pytest
python -m pytest tests checks -v
```

**Expect:** Respectively `3 passed`, `6 passed`, and `12 passed` if you wrote only
the required tests. The last command includes the six supplied acceptance cases.
Extra student tests increase those totals. Addition must continue to pass.

**If different:** Check argument order and return values. The negative-result case
helps detect reversed subtraction or an inappropriate absolute value. Preserve
the expected values and checks; fix the implementation when it is wrong.

Follow [the task workflow](../docs/WALKTHROUGH.md#4-repeat-for-addition-subtraction-and-delivery)
to commit and merge. Assessment Tests should now pass on your fork's `main`.
Complete the delivery task even if CI is already green.
