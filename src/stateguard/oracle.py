"""Independent transaction replay oracle for inventory systems."""


def replay_stock(initial_quantity: int, transactions: list[dict]) -> int:
    """Calculate the expected stock balance from submitted transactions.

    This function deliberately does not use the target application's
    inventory logic or its recorded stock changes.
    """

    if initial_quantity < 0:
        raise ValueError("Initial quantity cannot be negative.")

    expected_quantity = initial_quantity

    for transaction in transactions:
        kind = transaction["kind"]
        quantity = transaction["quantity"]

        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise ValueError("Transaction quantity must be an integer.")

        if kind in ("in", "return"):
            if quantity <= 0:
                raise ValueError("Stock-in and return quantities must be positive.")
            change = quantity

        elif kind == "out":
            if quantity <= 0:
                raise ValueError("Stock-out quantity must be positive.")
            change = -quantity

        elif kind == "adjust":
            change = quantity
            if change == 0:
                raise ValueError("An adjustment cannot be zero.")

        else:
            raise ValueError(f"Unknown movement type: {kind}")

        expected_quantity += change

        if expected_quantity < 0:
            raise ValueError("Transaction would produce negative stock.")

    return expected_quantity
