# Issue 4 — Document, verify, and deliver

## Objective

Make your work usable by another developer and submit verifiable evidence. Work on
branch `delivery`, starting from your updated `main`.

## Acceptance checklist

- [ ] PROJECT includes my name, purpose, setup and test commands, and links to all four issues.
- [ ] PROJECT explains one assertion and why `.venv` is ignored.
- [ ] All six student tests and supplied acceptance cases pass locally.
- [ ] All four tasks are merged into my fork's `main`; all four issues are closed.
- [ ] No environment or generated cache files are tracked.
- [ ] Assessment Tests ran and passed on the final pushed `main` commit.
- [ ] I submit my repository URL and its matching successful run URL.

## Instructions

**Where:** Editor, `PROJECT.md`.

**Do:** Include your title, name, and purpose; commands to create/select the
environment, install `requirements.txt`, and run both the student and complete test
suites; links to all four issues in your fork; and your short explanation of one
test's inputs, expected result, and assertion. Keep the `.venv` explanation from
Task 1. Use commands you actually ran. No long report or screenshots are required.

**Where:** Terminal, project root.

```bash
python -m pytest
python -m pytest tests checks -v
git ls-files
git status
```

**Expect:** All tests pass. Tracked files include your implementation, tests, setup,
and documentation; they exclude `.venv`, caches, and bytecode. Review, commit,
push, and merge the delivery branch using [the task workflow](../docs/WALKTHROUGH.md#4-repeat-for-addition-subtraction-and-delivery).
Close the issue after merging and checking the final files.

**Where:** Browser, your fork's Actions tab.

**Do:** Open **Assessment Tests** for your final `main` commit. Inspect the executed
`assessment` job and its last verification step. Submit using the
[final checklist](../docs/SUBMISSION.md).

**If different:** A Materials Check success is not your assessment result. A red
assessment run needs a fix, commit, push, and new run. Follow the failed step's
message rather than changing or disabling the supplied grading tools.
