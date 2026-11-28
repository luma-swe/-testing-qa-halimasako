# StateGuard — Project Proposal

## 1. Project Title and Category

**Project title:** StateGuard: An Automated State and Transaction Consistency Testing Tool

**Project category:** Software Testing and Quality Assurance

StateGuard is a Python-based testing tool designed to detect functional defects, invalid state transitions and data consistency problems in applications that maintain changing records over time.

The project will use an inventory management application as its target, focusing particularly on stock operations and transaction history.

## 2. Problem Statement and Motivation

Traditional software testing often focuses on whether individual operations produce the expected responses. However, an application can return successful responses while maintaining incorrect internal data.

This is particularly important in inventory management systems. A stock operation affects several related pieces of information: the product's current quantity, the transaction record and the historical quantity snapshots associated with that transaction.

For example, when a product has 10 units and a user records a stock-out of 4 units, the expected result is 6 units. The transaction history should also record a change of -4, a previous quantity of 10 and a resulting quantity of 6.

A defect could cause the application to update the product quantity incorrectly, record an incorrect transaction, or modify historical information. Individual API response checks may not detect all these problems.

StateGuard aims to address this issue through automated testing, controlled defect injection and an independent transaction-replay oracle.

## 3. What Will Be Built

### A. Existing Open-Source Software Under Test

StateGuard will test **Stockroom**, an open-source inventory management application.

- **Repository:** https://github.com/preransai/stockroom
- **Licence:** MIT
- **Pinned version:** `71253fceea005dd0dc8130136cc76cf4f0d92d60`
- **Technologies:** Flask, Python, SQLite and SQLAlchemy.

Stockroom provides product management, stock movements, inventory adjustments, stock alerts and reporting.

Its `StockMovement` model maintains a transaction ledger containing information such as movement type, signed quantity change, previous quantity (`qty_before`) and resulting quantity (`qty_after`).

The application will be kept at the specified Git commit to ensure a reproducible testing baseline. Controlled defects will be introduced on a separate working branch without modifying the pinned baseline.

StateGuard will interact with Stockroom through its HTTP interface and inspect its SQLite database in read-only mode when verifying internal state.

### B. StateGuard Testing Tool

StateGuard will be developed in Python and will include:

1. **HTTP Test Runner:** Sends requests to the target application and records responses, expected results and actual results.
2. **Test Cases:** Executes functional, input validation, state transition and data consistency tests.
3. **Transaction Log:** Maintains an independent record of the operations submitted by StateGuard.
4. **Transaction-Replay Oracle:** Recalculates expected inventory quantities independently and compares them against the application's recorded state.
5. **Snapshot Integrity Checks:** Detects changes to historical transaction snapshots after subsequent operations.
6. **Test Reporting:** Displays test names, expected results, actual results and PASS/FAIL outcomes.

### C. Independent Transaction-Replay Oracle

The transaction-replay oracle will be one of StateGuard's central features.

It will establish a known initial stock quantity and maintain its own expected transaction history based on the operations submitted by the testing tool.

For each operation, it will independently calculate the expected signed quantity change and resulting inventory balance.

For example, starting with 10 units:

| Operation | Expected balance |
|---|---:|
| Initial quantity | 10 |
| Stock-in: 15 | 25 |
| Stock-out: 4 | 21 |
| Return: 1 | 22 |
| Adjustment: -2 | 20 |

StateGuard will then compare its independently calculated results with:

- The recorded movement type and quantity change.
- The movement's `qty_before` and `qty_after` snapshots.
- The final quantity stored in the product record.
- Previously recorded snapshots, to ensure they remain unchanged after later transactions.

The oracle will derive expected changes from the original operations submitted by StateGuard, rather than trusting the application's recorded transaction values.

### D. Planned Defects

A total of **12 controlled defects** will be introduced into the target application, one at a time where appropriate, to evaluate StateGuard's detection capabilities.

The planned defect categories include:

1. Empty or missing input accepted.
2. Invalid quantity accepted.
3. Incorrect input boundary handling.
4. Incorrect stock-in calculation.
5. Incorrect stock-out calculation.
6. Incorrect return or adjustment behaviour.
7. Negative inventory permitted.
8. Incorrect `qty_before` snapshot.
9. Incorrect `qty_after` snapshot.
10. Product quantity and transaction ledger become inconsistent.
11. Failed transactions do not roll back all related changes.
12. Security or authorization validation bypassed, where supported by the target functionality.

Each defect will be documented with its intended behaviour, injected fault, corresponding test and detection result.

### E. Technologies

- Python
- pytest
- Flask
- SQLite
- SQLAlchemy
- Git and GitHub
- HTTP requests and JSON
- Terminal-based test reporting

## 4. Success Metrics

StateGuard will be evaluated using the following criteria:

- Successfully executes automated tests against the target application.
- Detects the 12 deliberately injected defects.
- Correctly identifies invalid input and boundary violations.
- Detects inconsistencies between submitted transactions, historical snapshots and current product quantities.
- Detects modifications to previously recorded transaction snapshots.
- Verifies that failed operations do not leave inconsistent partial updates.
- Produces understandable PASS/FAIL results with expected and actual outcomes.
- Can execute the test suite repeatedly against the pinned application version.

The main evaluation metric will be whether StateGuard can detect the deliberately injected defects and report the associated failures accurately.

## 5. Originality and Related Work

Existing automated testing frameworks such as pytest provide mechanisms for executing tests and checking expected results. Inventory applications may also include their own validation and consistency tests.

Stockroom, for example, already contains tests that verify whether its demo transaction history forms an unbroken ledger.

StateGuard builds on these ideas by introducing a separate testing tool that maintains its own expected transaction history and independently replays submitted operations.

Its focus is not limited to checking whether the application's own records are internally consistent. It also checks whether those records agree with the original operations submitted to the application.

The combination of independent transaction replay, historical snapshot integrity checks and controlled defect injection will form the project's main contribution.

## 6. Course Concepts and AI Tools

The project will apply concepts from the Software Testing and Quality Assurance course, including:

- Functional testing.
- Input validation and boundary value analysis.
- Equivalence partitioning.
- State transition testing.
- Assertions and test oracles.
- Data consistency and integrity testing.
- Regression testing.
- Negative testing and error handling.
- Defect injection and detection.

AI tools may be used as development and learning assistance for understanding existing code, debugging, generating test ideas and reviewing implementation choices. All generated suggestions and test results will be reviewed and verified.

## 7. Five-Week Checkpoint Plan

### Checkpoint 1 — Target Integration and Initial Prototype

**Objective:** Establish the testing environment and connect StateGuard to the selected application.

Tasks:
- Pin and document the Stockroom version.
- Set up the target application and its testing database.
- Adapt the StateGuard HTTP runner to interact with Stockroom.
- Implement the initial test execution and PASS/FAIL reporting.
- Establish authentication for test requests.
- Identify the product and stock movement data needed by StateGuard.
- Introduce and detect the first controlled defect.

**Deliverables:**
- Reproducible target application setup.
- Working HTTP test runner.
- Initial test cases and execution results.
- First defect detection demonstration.

**Defects:** 1 introduced and detected (1 cumulative).

### Checkpoint 2 — Input Validation and Functional Testing

**Objective:** Expand StateGuard's ability to detect incorrect input handling and basic functional defects.

Tasks:
- Implement tests for missing, empty and invalid inputs.
- Apply boundary value analysis to quantity fields.
- Test valid and invalid stock operations.
- Verify expected HTTP status codes and response content.
- Test quantity limits and rejection of invalid stock operations.
- Introduce controlled input validation and functional defects.

**Deliverables:**
- Expanded test suite.
- Input validation and boundary tests.
- Defect detection results.
- Checkpoint test report.

**Defects:** 3 additional defects (4 cumulative).

### Checkpoint 3 — Transaction Replay and Data Consistency

**Objective:** Implement the independent transaction-replay oracle.

Tasks:
- Maintain an independent record of submitted stock operations.
- Establish known initial inventory quantities.
- Calculate expected stock balances independently.
- Retrieve and inspect the application's recorded transaction history.
- Compare expected changes with recorded movement values.
- Verify `qty_before`, `qty_after` and final product quantities.
- Test sequences of stock-in, stock-out, returns and adjustments.
- Introduce defects affecting transaction calculations and consistency.

**Deliverables:**
- Working transaction-replay oracle.
- Automated ledger consistency tests.
- Multi-operation transaction scenarios.
- Defect detection results and report.

**Defects:** 3 additional defects (7 cumulative).

### Checkpoint 4 — Historical Snapshot Integrity and State Transitions

**Objective:** Extend StateGuard to detect defects affecting historical records and related state changes.

Tasks:
- Verify that historical movement snapshots remain unchanged after subsequent operations.
- Test consecutive stock movements and adjustment sequences.
- Verify consistency between product records and transaction history.
- Test failed operations and rollback behaviour.
- Test relevant authorization and state transition rules.
- Introduce defects affecting historical snapshots, transaction rollback and state handling.

**Deliverables:**
- Snapshot integrity tests.
- Extended state transition tests.
- Rollback and authorization test cases.
- Defect detection results and report.

**Defects:** 3 additional defects (10 cumulative).

### Checkpoint 5 — Regression Testing and Final Evaluation

**Objective:** Consolidate the tool and evaluate its overall effectiveness.

Tasks:
- Integrate all test modules into a complete regression suite.
- Run the complete suite against the target application.
- Introduce and detect the final controlled defects.
- Verify that previously detected defects remain detectable.
- Review test coverage and false-positive results.
- Improve test reporting and documentation.
- Document limitations, findings and possible future improvements.

**Deliverables:**
- Complete StateGuard testing tool.
- Final automated regression suite.
- Results for all 12 injected defects.
- Final project report and demonstration.

**Defects:** 2 additional defects (12 cumulative).