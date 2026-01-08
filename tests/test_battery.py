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
