from battery import BatteryChecker

def test_can_create_battery_checker():
    checker = BatteryChecker()
    assert checker is not None