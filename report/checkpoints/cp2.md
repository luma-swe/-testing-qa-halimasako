# Checkpoint 2 — Input Validation and Test Execution

## 1. Objective

The objective of Checkpoint 2 was to improve the StateGuard test execution mechanism, implement input validation tests, cover invalid and boundary-value inputs, and demonstrate defect detection using controlled defects in the target application.

## 2. Test Runner Improvements

The StateGuard test runner (`src/stateguard/runner.py`) was improved to support optional expected response-body checking.

The `run_test()` function now accepts an `expected_body` parameter. When provided, the runner checks both:
- Whether the actual HTTP status matches the expected status.
- Whether the expected text is present in the response body.

The `TestResult` dataclass also stores the expected response body.

This allows StateGuard to check more than HTTP status codes when evaluating API responses.

## 3. Input Validation Tests

Six automated tests were implemented in `tests/test_input_val.py`.

| Test | Input / Scenario | Expected HTTP status |
|---|---|---:|
| `test_reject_empty_name` | Empty item name | 400 |
| `test_reject_quantity_above_maximum` | Quantity = 1,000,001 | 400 |
| `test_accept_maximum_quantity` | Quantity = 1,000,000 | 201 |
| `test_accept_zero_quantity` | Quantity = 0 | 201 |
| `test_reject_negative_quantity` | Quantity = -1 | 400 |
| `test_reject_description_above_maximum` | Description length = 1,001 characters | 400 |

These tests cover invalid inputs, valid inputs, and important boundary values.

## 4. Controlled Defect Detection

Four controlled defects were introduced individually in the target application's validation logic to evaluate StateGuard's ability to detect incorrect API behavior.

| Defect | Description | Detection test |
|---|---|---|
| D01 | Negative quantity of -1 was incorrectly accepted | `test_reject_negative_quantity` |
| D02 | Empty item names were incorrectly accepted | `test_reject_empty_name` |
| D03 | Quantities above 1,000,000 were incorrectly accepted | `test_reject_quantity_above_maximum` |
| D04 | Descriptions longer than 1,000 characters were incorrectly accepted | `test_reject_description_above_maximum` |

For each defect, the corresponding test detected the incorrect HTTP response. The affected validation condition was then restored.

D01 remains intentionally active from Checkpoint 1. Its test verifies that StateGuard reports the incorrect response as a failed test result.

D02, D03, and D04 were restored after their individual detection experiments.

## 5. Final Test Results

After restoring D02, D03, and D04, the six tests in `tests/test_input_val.py` were executed again