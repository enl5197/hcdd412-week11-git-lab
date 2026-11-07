"""Late-fee calculation for the campus library desk."""


def late_fee(days_late: int, daily_rate: float, grace_days: int = 0) -> float:
    """Return the late fee in dollars for an item returned ``days_late`` days late.

    The first ``grace_days`` days late are free. Only days beyond the grace
    period are charged. Items returned on time or early are never charged.
    """
    billable_days = max(0, days_late - grace_days)
    return round(billable_days * daily_rate, 2)
