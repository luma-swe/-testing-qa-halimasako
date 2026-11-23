
from stateguard import run_test


BASE_URL = "http://127.0.0.1:5000"


def test_create_item_with_valid_data():
    result = run_test(
        base_url=BASE_URL,
        name="Create item with valid data",
        method="POST",
        path="/items",
        expected_status=201,
        json_body={
            "name": "Notebook",
            "description": "Grid paper",
            "quantity": 3,
        },
    )

    assert result.passed is True


def test_negative_quantity_defect_is_detected():
    result = run_test(
        base_url=BASE_URL,
        name="Reject negative quantity",
        method="POST",
        path="/items",
        expected_status=400,
        json_body={
            "name": "Notebook",
            "quantity": -1,
        },
    )

    assert result.passed is False
    assert result.actual_status == 201
