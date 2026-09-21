# Issue 1 — Set up a reproducible Python project

## Objective

Create and select a project virtual environment, install the supplied dependencies,
and configure pytest. Use the `setup` branch and reference your actual issue number.

## Acceptance checklist

- [ ] `.venv` exists locally and the selected Python executable is inside it.
- [ ] `requirements.txt` and `pytest.ini` are copied from `provided/` to the root.
- [ ] `python -m pytest --version` reports `pytest 8.4.2`.
- [ ] `.venv` and caches are ignored, not staged or committed.
- [ ] PROJECT explains why the environment is local but requirements are committed.
- [ ] Setup work is committed, pushed, merged into my fork's `main`, and the issue closed.

## Instructions

**Where:** Terminal, at the cloned repository root, on your `setup` branch.

The starter already supplies `.gitignore`, workflows, and grading tools. Preserve
them. Copy the supplied configuration and create/select the environment.

**Do — macOS/Linux (bash or zsh):**

```bash
cp provided/requirements.txt requirements.txt
cp provided/pytest.ini pytest.ini
python3 -m venv .venv
source .venv/bin/activate
```

**Do — Windows PowerShell:**

```powershell
Copy-Item provided/requirements.txt requirements.txt
Copy-Item provided/pytest.ini pytest.ini
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Do — either platform, after activation:**

```bash
python --version
python -c "import sys; print(sys.executable)"
python -m pip install -r requirements.txt
python -m pytest --version
git status --short
git check-ignore .venv/pyvenv.cfg
```

**Expect:** Python 3.13, an executable path inside this project's `.venv`, and
`pytest 8.4.2`. The ignore check prints `.venv/pyvenv.cfg`; that directory does not
appear among files to stage. Installing requirements installs packages into your
environment; copying the file alone does not install anything.

Open `pytest.ini`. Under `[pytest]`, `testpaths = tests` selects student tests and
`pythonpath = .` supports importing your package from the root. You may copy this
configuration; you do not need to memorize it.

**If different:** If PowerShell blocks activation, invoke
`.\.venv\Scripts\python.exe` instead of `python` in subsequent commands. Select
that interpreter in your editor too. On macOS/Linux the direct path is
`.venv/bin/python`. Ask for help if the installed Python version differs.

**Where:** Editor, `PROJECT.md`.

**Do:** Explain in one or two sentences why requirements are committed and `.venv`
is ignored. Save and follow [the setup review/merge sequence](../docs/WALKTHROUGH.md#3-complete-issue-1-setup).

There are no student tests yet. A full pytest run is not expected to pass at this
stage. The workflow stays red until all required project files and tests exist.
