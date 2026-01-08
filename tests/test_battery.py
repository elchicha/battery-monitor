from battery import BatteryChecker


def test_can_create_battery_checker():
    checker = BatteryChecker()
    assert checker is not None


def test_get_battery_percentage():
    checker = BatteryChecker()
    level = checker.get_percentage()
    assert isinstance(level, (int, float))
    assert level >= 0 and level <= 100


def test_get_charging_status():
    checker = BatteryChecker()
    is_charging = checker.is_charging()
    assert isinstance(is_charging, bool)


def test_get_time_remaining():
    checker = BatteryChecker()
    time_remaining = checker.get_time_remaining()
    # Time remaining could be None (if can't calculate) or a positive number
    print(f"Time left: {time_remaining} minutes")
    assert time_remaining is None or (
        isinstance(time_remaining, (int, float)) and time_remaining >= 0
    )
