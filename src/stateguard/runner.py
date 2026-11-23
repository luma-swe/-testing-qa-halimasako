
"""HTTP test runner for StateGuard."""

import json
from dataclasses import dataclass
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


@dataclass
class TestResult:
    name: str
    expected_status: int
    actual_status: int | None
    passed: bool
    response_body: str


def run_test(
    base_url: str,
    name: str,
    method: str,
    path: str,
    expected_status: int,
    json_body: dict | None = None,
) -> TestResult:
    """Send an HTTP request and compare its status with the expected status."""

    url = base_url.rstrip("/") + "/" + path.lstrip("/")

    data = None
    headers = {}

    if json_body is not None:
        data = json.dumps(json_body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = Request(
        url,
        data=data,
        headers=headers,
        method=method.upper(),
    )

    try:
        with urlopen(request, timeout=5) as response:
            actual_status = response.status
            response_body = response.read().decode("utf-8")

    except HTTPError as error:
        actual_status = error.code
        response_body = error.read().decode("utf-8")

    except URLError as error:
        actual_status = None
        response_body = str(error.reason)

    passed = actual_status == expected_status

    return TestResult(
        name=name,
        expected_status=expected_status,
        actual_status=actual_status,
        passed=passed,
        response_body=response_body,
    )
