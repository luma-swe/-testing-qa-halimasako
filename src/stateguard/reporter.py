
"""Display StateGuard test results."""


def print_report(results: list) -> None:
    """Print individual test results and a summary."""

    passed = sum(result.passed for result in results)
    failed = len(results) - passed

    print("\nStateGuard Test Report")
    print("----------------------")

    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"[{status}] {result.name}")

        if not result.passed:
            print(f"       Expected HTTP: {result.expected_status}")
            print(f"       Actual HTTP:   {result.actual_status}")

    print("----------------------")
    print(f"Results: {passed} passed, {failed} failed")
