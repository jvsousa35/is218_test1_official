# IS 218 Test 1 — Calculator Project

**Student:** John Sousa  
**Project:** Build, Test, and Deliver a Python Calculator

## Purpose

This project is a small Python calculator package that implements addition and subtraction. The project also includes pytest tests that verify the required calculator behavior and make the project reproducible for another developer.

## Project Setup

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### Windows PowerShell

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

The `requirements.txt` file is committed so another developer can install the same required dependency version. The `.venv` folder is ignored because it is a machine-specific local environment that can be recreated from `requirements.txt` and should not be stored in Git.

## Run the Tests

Run the six student tests:

```bash
python -m pytest
```

Run both the student tests and the supplied acceptance checks:

```bash
python -m pytest tests checks -v
```

The expected result with only the required tests is six passing student tests and twelve passing tests when the supplied acceptance checks are included.

## Required Issues

The required GitHub issues for this project are linked below. If GitHub assigns different issue numbers, update the issue numbers to match the issues created in the repository.

1. [Issue 1 — Set up a reproducible Python project](https://github.com/jvsousa35/is218_test1_official/issues/1)
2. [Issue 2 — Implement and test addition](https://github.com/jvsousa35/is218_test1_official/issues/2)
3. [Issue 3 — Implement and test subtraction](https://github.com/jvsousa35/is218_test1_official/issues/3)
4. [Issue 4 — Document, verify, and deliver](https://github.com/jvsousa35/is218_test1_official/issues/4)

## Assertion Explanation

In `test_add`, the calculator is called with the inputs `2` and `3`. The expression `assert add(2, 3) == 5` verifies that the `add` function returns the expected value of `5`. If the function returns any other value, pytest reports the test as failed.

## Calculator Behavior

- `add(a, b)` returns `a + b`.
- `subtract(a, b)` returns `a - b`.

## Final Verification

Before submitting, run:

```bash
python -m pytest
python -m pytest tests checks -v
git ls-files
git status
```

Then confirm that the final commit on your fork's `main` branch has a successful **Assessment Tests** GitHub Actions run. Submit both the fork URL and the matching successful Actions run URL.
