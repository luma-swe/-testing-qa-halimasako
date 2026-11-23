# Checkpoint 1 – Project Setup and Initial Prototype


## 1. Project Structure

The initial StateGuard implementation consists of:

- `src/stateguard/runner.py`: Sends HTTP requests and compares actual and expected status codes.
- `src/stateguard/reporter.py`: Displays test results and execution summaries.
- `src/stateguard/__init__.py`: Exposes the main StateGuard functions.
- `src/stateguard/__main__.py`: Provides an executable entry point.
- `tests/test_runner.py`: Contains automated tests for the runner.

## 2. Initial Prototype

The initial prototype supports:

1. Sending HTTP requests to a running API.
2. Supporting different HTTP methods.
3. Sending JSON request bodies.
4. Capturing successful and error HTTP responses.
5. Comparing actual HTTP status codes with expected status codes.
6. Reporting individual test results.

## 3. Controlled Defect D01

One controlled defect was introduced into the target application's input validation mechanism.

**Defect:** Negative quantities are incorrectly accepted when the quantity is exactly -1.

Original validation condition:

`quantity < 0`

Modified validation condition:

`quantity < -1`

As a result, a request containing a quantity of -1 is accepted instead of being rejected.

## 4. Testing and Results

The original target application passed all 17 of its existing tests before defect injection.

After introducing D01:

- 16 original application tests passed.
- 1 original application test failed, confirming the changed validation behaviour.

Two StateGuard integration tests were implemented:

| Test | Expected result | Outcome |
|---|---|---|
| Create item with valid data | HTTP 201 | PASS |
| Reject negative quantity (D01) | HTTP 400 | FAIL detected by StateGuard |

The StateGuard test suite itself reported **2 passed**. The second test passes because it successfully confirms that StateGuard detects the incorrect HTTP 201 response.

