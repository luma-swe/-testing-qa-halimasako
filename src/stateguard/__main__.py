
"""Run the StateGuard demonstration tests."""

from stateguard import print_report, run_test


def main() -> None:
    base_url = "http://127.0.0.1:5000"

    results = [
        run_test(
            base_url=base_url,
            name="Create item with valid data",
            method="POST",
            path="/items",
            expected_status=201,
            json_body={"name": "Pen", "quantity": 2},
        ),
        run_test(
            base_url=base_url,
            name="Reject negative quantity (D01)",
            method="POST",
            path="/items",
            expected_status=400,
            json_body={"name": "Notebook", "quantity": -1},
        ),
    ]

    print_report(results)


if __name__ == "__main__":
    main()
