"""Validate the distributed handout without requiring a completed student solution."""

import ast
import configparser
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


REQUIRED = [
    "README.md", "SPEC.md", "AGENTS.md", ".gitignore",
    "docs/WALKTHROUGH.md", "docs/SUBMISSION.md", "docs/TROUBLESHOOTING.md",
    "tasks/01-setup.md", "tasks/02-addition.md", "tasks/03-subtraction.md", "tasks/04-delivery.md",
    "instructor/README.md", "provided/requirements.txt", "provided/pytest.ini",
    ".github/workflows/materials.yml", ".github/workflows/tests.yml",
    "scripts/check_materials.py", "scripts/check_project.py", "scripts/check_results.py",
    "checks/test_contract.py",
]


def main():
    errors = []
    for name in REQUIRED:
        path = Path(name)
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"Missing or empty supplied material: {name}")
    for name in REQUIRED:
        path = Path(name)
        if not path.is_file():
            continue
        if path.suffix == ".py":
            try:
                ast.parse(path.read_text(encoding="utf-8"), filename=name)
            except SyntaxError as exc:
                errors.append(f"Invalid supplied Python: {exc}")
        if path.suffix == ".md":
            prose = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
            for target in re.findall(r"\]\(([^\s)]+)\)", prose):
                parsed = urlsplit(target)
                if parsed.scheme or target.startswith("#"):
                    continue
                destination = path.parent / unquote(parsed.path)
                if not destination.exists():
                    errors.append(f"Broken relative link in {name}: {target}")
    config = configparser.ConfigParser()
    try:
        config.read("provided/pytest.ini")
        for key, expected in [("testpaths", "tests"), ("pythonpath", ".")]:
            if config.get("pytest", key, fallback="").strip() != expected:
                errors.append(f"provided/pytest.ini must set {key} = {expected}.")
    except configparser.Error as exc:
        errors.append(f"Invalid provided configuration: {exc}")
    text = "## Materials Check\n\n"
    if errors:
        text += "\n".join(f"- {error}" for error in errors) + "\n"
    else:
        text += "Supplied files, Python syntax, configuration, and relative file links passed.\n"
    text += "\nThis checks assessment materials, not a completed student submission.\n"
    print(text)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as handle:
            handle.write(text)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
