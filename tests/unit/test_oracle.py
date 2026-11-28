import pytest

from stateguard.oracle import replay_stock


def test_stock_out():
    assert replay_stock(
        18,
        [{"kind": "out", "quantity": 2}],
    ) == 16


def test_stock_in():
    assert replay_stock(
        10,
        [{"kind": "in", "quantity": 5}],
    ) == 15


def test_return():
    assert replay_stock(
        10,
        [{"kind": "return", "quantity": 3}],
    ) == 13


def test_adjustment():
    assert replay_stock(
        10,
        [{"kind": "adjust", "quantity": -2}],
    ) == 8


def test_multiple_transactions():
    transactions = [
        {"kind": "in", "quantity": 5},
        {"kind": "out", "quantity": 3},
        {"kind": "return", "quantity": 2},
        {"kind": "adjust", "quantity": -1},
    ]

    assert replay_stock(10, transactions) == 13


def test_reject_negative_stock():
    with pytest.raises(ValueError):
        replay_stock(2, [{"kind": "out", "quantity": 3}])


def test_reject_zero_stock_out():
    with pytest.raises(ValueError):
        replay_stock(10, [{"kind": "out", "quantity": 0}])


def test_reject_unknown_movement():
    with pytest.raises(ValueError):
        replay_stock(10, [{"kind": "transfer", "quantity": 2}])


def test_reject_boolean_quantity():
    with pytest.raises(ValueError):
        replay_stock(10, [{"kind": "out", "quantity": True}])
