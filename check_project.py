"""Check committed project files and reproducible setup using the standard library."""

import configparser
import os
from pathlib import Path, PurePosixPath
import subprocess


def main():
    tracked = set(subprocess.check_output(["git", "ls-files", "-z"], text=True).split("\0"))
    required = [
        "README.md", "PROJECT.md", ".gitignore", "requirements.txt", "pytest.ini",
        "calculator/__init__.py", "tests/operations/test_add.py",
        "tests/operations/test_subtract.py", ".github/workflows/tests.yml",
        "scripts/check_project.py", "scripts/check_results.py", "checks/test_contract.py",
    ]
    errors = []
    rows = ["## Project readiness", "", "| File | Status |", "| --- | --- |"]
    for name in required:
        path = Path(name)
        ok = name in tracked and path.is_file() and path.stat().st_size > 0
        rows.append(f"| `{name}` | {'Present' if ok else 'Missing, empty, or untracked'} |")
        if not ok:
            errors.append(f"Create, save, and commit the required nonempty file: {name}")

    config = configparser.ConfigParser()
    try:
        config.read("pytest.ini")
        for key, value in [("testpaths", "tests"), ("pythonpath", ".")]:
            if config.get("pytest", key, fallback="").strip() != value:
                errors.append(f"Set {key} = {value} under [pytest] in pytest.ini.")
    except configparser.Error as exc:
        errors.append(f"Correct pytest.ini: {exc}")

    forbidden = {".venv", "venv", "env", ".env", "__pycache__", ".pytest_cache"}
    for name in sorted(filter(None, tracked)):
        path = PurePosixPath(name)
        if (forbidden.intersection(path.parts[:-1]) or path.name == "pyvenv.cfg"
                or path.suffix in {".pyc", ".pyo", ".pyd"}):
            errors.append(f"Untrack generated file (keep the local copy): {name}")

    probes = [".venv/probe.txt", "calculator/__pycache__/probe.txt", ".pytest_cache/probe.txt",
              "calculator/probe.pyc", "calculator/probe.pyo", "calculator/probe.pyd"]
    for name in probes:
        result = subprocess.run(
            ["git", "-c", f"core.excludesFile={os.devnull}", "check-ignore", "--no-index", "-q", name]
        )
        if result.returncode:
            errors.append(f"Restore the supplied .gitignore so it excludes {name}.")

    if errors:
        rows.extend(["", "### Work still needed", ""] + [f"- {error}" for error in errors])
    else:
        rows.extend(["", "Required files, pytest configuration, and Git hygiene passed."])
    summary = "\n".join(rows) + "\n"
    print(summary)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as handle:
            handle.write(summary)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
