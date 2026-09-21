"""Verify executed test results, not merely pytest's successful exit status."""

import os
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


STUDENT_TESTS = {
    ("tests.operations.test_add", "test_add"),
    ("tests.operations.test_add", "test_add_zero"),
    ("tests.operations.test_add", "test_add_negative"),
    ("tests.operations.test_subtract", "test_subtract"),
    ("tests.operations.test_subtract", "test_subtract_negative_result"),
    ("tests.operations.test_subtract", "test_subtract_zero"),
}
CONTRACT_TESTS = {
    ("checks.test_contract", "test_add_contract[2-3-5]"),
    ("checks.test_contract", "test_add_contract[7-0-7]"),
    ("checks.test_contract", "test_add_contract[-4-1--3]"),
    ("checks.test_contract", "test_subtract_contract[5-3-2]"),
    ("checks.test_contract", "test_subtract_contract[3-5--2]"),
    ("checks.test_contract", "test_subtract_contract[7-0-7]"),
}


def main(report_path):
    path = Path(report_path)
    if not path.is_file():
        print("No test report was produced. Fix the earlier failed step and push again.")
        return 1
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        print(f"Invalid test report: {exc}")
        return 1
    passed = set()
    unsuccessful = set()
    for case in root.iter("testcase"):
        identity = (case.get("classname"), case.get("name"))
        if any(child.tag in {"failure", "error", "skipped"} for child in case):
            unsuccessful.add(identity)
        else:
            passed.add(identity)
    missing = (STUDENT_TESTS | CONTRACT_TESTS) - (passed - unsuccessful)
    lines = ["## Assessment test results", "", "| Required test | Result |", "| --- | --- |"]
    for module, name in sorted(STUDENT_TESTS | CONTRACT_TESTS):
        status = "PASS" if (module, name) not in missing else "NOT PASSED"
        lines.append(f"| `{module}::{name}` | {status} |")
    lines.extend(["", "All 6 student tests and 6 acceptance cases must run and pass without skips or xfail."])
    if not missing:
        lines.append("Automated requirements passed. Instructor review completes the grade.")
    output = "\n".join(lines) + "\n"
    print(output)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as handle:
            handle.write(output)
    return 1 if missing else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/check_results.py PATH_TO_JUNIT_XML")
    raise SystemExit(main(sys.argv[1]))
