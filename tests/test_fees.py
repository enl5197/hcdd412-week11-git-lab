
from campusfees import late_fee


def test_on_time_return_is_free():
    assert late_fee(0, 0.25) == 0.0


def test_early_return_is_free():
    assert late_fee(-2, 0.25) == 0.0


def test_late_fee_within_grace_period():
    assert late_fee(2, 0.50, grace_days=3) == 0.0


def test_late_fee_past_grace_period():
    assert late_fee(5, 0.50, grace_days=3) == 1.0


def test_maximum_fee_is_enforced():
    assert late_fee(5, 0.50, max_fee=1.00) == 1.00


def test_fee_below_maximum_is_unchanged():
    assert late_fee(2, 0.25, max_fee=1.00) == 0.50


def test_grace_period_and_maximum_fee_work_together():
    assert late_fee(7, 0.50, grace_days=3, max_fee=1.00) == 1.00
