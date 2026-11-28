from stateguard import run_test

BASE_URL = "http://127.0.0.1:5000"


def test_reject_empty_name():
    result = run_test(
        base_url=BASE_URL,
        name="Reject empty name",
        method="POST",
        path="/items",
        expected_status=400,
        json_body={
            "name": "",
            "quantity": 5,
        },
    )

    assert result.actual_status == 400

def test_reject_quantity_above_maximum():
    result = run_test(
        base_url=BASE_URL,
        name="Reject quantity above maximum",
        method="POST",
        path="/items",
        expected_status=400,
        json_body={
            "name": "Notebook",
            "quantity": 1_000_001,
        },
    )   

    assert result.actual_status == 400

def test_accept_maximum_quantity():
    result = run_test(
        base_url=BASE_URL,
        name="Accept maximum quantity",
        method="POST",
        path="/items",
        expected_status=201,
        json_body={
            "name": "Notebook",
            "quantity": 1_000_000,
        },
    )

    assert result.actual_status == 201

def test_accept_zero_quantity():
    result = run_test(
        base_url=BASE_URL,
        name="Accept zero quantity",
        method="POST",
        path="/items",
        expected_status=201,
        json_body={
            "name": "Notebook",
            "quantity": 0,
        },
    )

    assert result.actual_status == 201

def test_reject_negative_quantity():
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

def test_reject_description_above_maximum():
    result = run_test(
        base_url=BASE_URL,
        name="Reject description above maximum",
        method="POST",
        path="/items",
        expected_status=400,
        json_body={
            "name": "Notebook",
            "description": "A" * 1001,
            "quantity": 5,
        },
    )

    assert result.actual_status == 400    