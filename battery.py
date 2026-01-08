class BatteryChecker:
    def __init__(self):
        self.level = 0

    def get_percentage(self):
        """Retrieve the battery percentage level.

        Returns:
            int or float: Battery percentage level.
        """
        with open("/sys/class/power_supply/BAT0/capacity") as capacity_file:
            self.level = int(capacity_file.read().strip())
        return self.level

    def is_charging(self):
        """Check if the battery is currently charging.

        Returns:
            bool: True if charging, False otherwise.
        """
        with open("/sys/class/power_supply/BAT0/status") as status_file:
            status = status_file.read().strip()
        return status == "Charging"
