# StateGuard: Automated Testing and Defect Detection for Existing Software

## 1. Project Title and Category

**Project Title:** StateGuard: Automated Testing and Defect Detection for Existing Software

**Project Category:** Software Testing Tool / Automated Testing / Defect Detection

## 2. Problem Statement and Motivation

Software applications may contain functional defects, input validation errors, incorrect state transitions, data inconsistencies and security-related vulnerabilities. These issues can cause unexpected behaviour, incorrect results or potentially unsafe operations.

Although existing testing frameworks allow developers to write and execute tests, identifying different types of defects and systematically evaluating their detection can require considerable manual effort.

This project aims to develop StateGuard, an automated testing tool that evaluates an existing software application using predefined test scenarios and deliberately injected defects.

Instead of developing a new application to test, the project will use an existing open-source application as its testing target. Twelve controlled defects will be introduced into the target application. StateGuard will execute corresponding test cases, compare actual behaviour with expected results, identify failures and generate a testing report.

The purpose is to evaluate how effectively the tool detects the injected defects and reports the resulting inconsistencies.

## 3. What Will Be Built

The project will consist of two separate components:

**A. Existing software under test**

An existing open-source application will be selected as the testing target. The application will be studied to understand its main features, normal behaviour and expected results.

Twelve controlled defects will be introduced into its code. These may include functional errors, input validation problems, incorrect data handling, boundary-condition errors and security-related issues, depending on the capabilities of the selected application.

**B. StateGuard testing tool**

StateGuard will be developed in Python. It will execute automated tests against the target application and evaluate whether its behaviour matches the expected results.

The tool will perform the following tasks:

1. **Test execution:** Execute predefined test cases against the target application.
2. **Input validation testing:** Submit valid, invalid, empty and boundary-value inputs.
3. **Functional testing:** Verify that the application's main operations produce the expected results.
4. **State and data consistency testing:** Check whether application data remains correct after sequences of operations.
5. **Error detection:** Identify unexpected behaviour, incorrect outputs and failed assertions.
6. **Defect detection:** Determine whether the injected defects are detected by the corresponding test cases.
7. **Test reporting:** Generate a report containing executed tests, passed and failed tests, detected defects and undetected defects.
8. **Detection evaluation:** Calculate the proportion of injected defects successfully detected by the tool.

### Planned Injected Defects

The project will include twelve deliberately introduced defects. Their exact implementation will depend on the selected application's architecture and available features.

The initial distribution will be:

| No. | Defect to inject | Expected behaviour |
|---|---|---|
| 1 | Empty input accepted | Required fields should reject empty values |
| 2 | Invalid input accepted | Invalid data should be rejected |
| 3 | Incorrect input boundary handling | Boundary values should be handled correctly |
| 4 | Incorrect creation operation | New records should be created accurately |
| 5 | Incorrect update operation | Updates should preserve data integrity |
| 6 | Incorrect deletion operation | Deleted records should no longer be accessible |
| 7 | Incorrect status transition | Only permitted state transitions should occur |
| 8 | Duplicate records permitted | Duplicate operations should follow defined rules |
| 9 | Incorrect search or filtering | Search results should match the requested criteria |
| 10 | Incorrect sorting or calculation | Results should follow the expected ordering or calculation |
| 11 | Incorrect error handling | Invalid operations should return appropriate errors |
| 12 | Security-related defect, where supported | The application should reject an unauthorized or unsafe operation |

These defects will be introduced individually or in controlled combinations so that their effects can be evaluated and reproduced.

### Technologies and Tools

- Python: implementation of StateGuard.
- Pytest: automated test execution and assertions.
- Hypothesis (if appropriate): generation of additional test inputs and edge cases.
- Git: version control.
- An existing open-source application: target software.
- The target application's existing technology stack: required to understand and introduce the defects.

## 4. Success Metrics

The project will be evaluated using the following criteria:

- All twelve planned defects are successfully introduced and documented.
- Each injected defect has at least one corresponding test scenario.
- StateGuard can execute the test suite against the selected application.
- The tool correctly identifies whether individual test cases pass or fail.
- The tool produces a report of detected and undetected defects.
- The final evaluation measures the percentage of injected defects detected.

The defect detection rate will be calculated as:

Detection Rate = (Number of detected injected defects / 12) × 100

The tool should also provide repeatable results when the same tests are executed under the same conditions.

## 5. Originality and Related Work

StateGuard builds upon established software testing practices and frameworks, including automated testing, test case design, assertion-based verification and defect detection.

Existing tools such as pytest provide the infrastructure for executing tests, while property-based testing frameworks such as Hypothesis can generate a wider range of inputs.

The project focuses on combining these practices into a testing workflow that evaluates an existing application against a controlled set of twelve deliberately injected defects.

The main objective is not to replace existing testing frameworks but to develop a structured tool that executes tests, evaluates their outcomes and measures defect detection effectiveness.

## 6. Course Concepts and Use of AI Tools

The project will apply several software testing and quality assurance concepts:

- Equivalence Partitioning
- Boundary Value Analysis
- Functional Testing
- Black-box and White-box Testing
- Test Case Design
- Test Oracles and Assertions
- State Transition Testing
- Negative Testing
- Regression Testing
- Defect Injection
- Test Reporting and Evaluation

AI tools may be used to assist with understanding unfamiliar code, reviewing test scenarios, debugging and documenting the project. All generated code and test results will be reviewed and verified by the student.

## 7. Implementation Plan and Weekly Checkpoints

The project will be developed over five consecutive weeks. Each checkpoint will deliver an incremental, working version of the project.

Every checkpoint must contain:

- Updated source code in `src/`.
- At least one automated test in `tests/`.
- A checkpoint report in `report/checkpoints/`.

The overall plan will be maintained in `report/plan.md`.

### Checkpoint 1 – Project Setup and Initial Prototype (Week 9)

**Objectives:**
- Select and study an existing open-source application.
- Understand its main features and expected behaviour.
- Set up the StateGuard project structure.
- Implement an initial testing prototype.
- Introduce the first controlled defect.

**Injected defects:** 1 defect.

**Tests:**
- Create at least one automated test for the selected application.
- Verify the expected behaviour of a normal operation.
- Test the behaviour affected by the first injected defect.

**Deliverables:**
- Initial working prototype in `src/`.
- At least one automated test in `tests/`.
- `report/checkpoints/cp1.md`.
- Updated `report/plan.md`.

### Checkpoint 2 – Test Execution and Input Validation (Week 10)

**Objectives:**
- Improve the test execution mechanism.
- Implement input validation tests.
- Add support for testing invalid and boundary-value inputs.
- Introduce additional controlled defects.

**Injected defects:** 3 additional defects (4 cumulative).

**Tests:**
- Valid and invalid input tests.
- Empty-field tests.
- Boundary-value tests.
- Tests verifying the detection of the newly injected defects.

**Deliverables:**
- Improved working prototype.
- Additional automated tests.
- `report/checkpoints/cp2.md`.

### Checkpoint 3 – Functional and Data Consistency Testing (Week 11)

**Objectives:**
- Extend StateGuard to test multiple application operations.
- Verify data consistency after sequences of operations.
- Test creation, modification and deletion behaviour.
- Introduce additional defects.

**Injected defects:** 3 additional defects (7 cumulative).

**Tests:**
- CRUD operation tests.
- State transition tests.
- Data consistency tests.
- Tests for the newly injected defects.

**Deliverables:**
- Extended testing functionality.
- Updated automated test suite.
- `report/checkpoints/cp3.md`.

### Checkpoint 4 – Extended Defect Detection and Reporting (Week 12)

**Objectives:**
- Add tests for more complex application behaviours.
- Improve error detection and test result classification.
- Implement automated test reporting.
- Introduce additional defects, including a security-related defect if supported by the target application.

**Injected defects:** 3 additional defects (10 cumulative).

**Tests:**
- Search, filtering or calculation tests, depending on the application.
- Error-handling tests.
- Security-related tests where applicable.
- Tests verifying the newly introduced defects.

**Deliverables:**
- Expanded testing tool.
- Initial automated test report.
- Updated test suite.
- `report/checkpoints/cp4.md`.

### Checkpoint 5 – Final Testing and Evaluation (Week 13)

**Objectives:**
- Introduce the final two defects.
- Complete the twelve-defect testing dataset.
- Execute the complete test suite.
- Evaluate StateGuard's defect detection performance.
- Fix remaining implementation problems and prepare the final documentation.

**Injected defects:** 2 additional defects (12 cumulative).

**Tests:**
- Full regression test suite.
- Tests for all twelve injected defects.
- Verification of repeatability.
- Evaluation of detected and undetected defects.

**Deliverables:**
- Final working version of StateGuard.
- Complete automated test suite.
- Final defect detection report.
- `report/checkpoints/cp5.md`.

