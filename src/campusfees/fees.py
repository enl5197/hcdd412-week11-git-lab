"""Late-fee calculation for the campus library desk."""

from typing import Optional


def late_fee(
    days_late: int,
    daily_rate: float,
    grace_days: int = 0,
    max_fee: Optional[float] = None,
) -> float:
    """Return the late fee in dollars for an item returned ``days_late`` days late.

    The first ``grace_days`` days late are free. Only days beyond the grace
    period are charged. Items returned on time or early are never charged.
    When ``max_fee`` is given, the fee never exceeds it.
    """
    billable_days = max(0, days_late - grace_days)
    fee = round(billable_days * daily_rate, 2)

    if max_fee is not None:
        fee = min(fee, max_fee)

    return fee
