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

    def get_time_remaining(self):
        """Estimate the remaining time until battery depletion.

        Returns:
            int or float or None: Estimated time remaining in minutes, or None if cannot be calculated.
        """
        charge_now = int(open("/sys/class/power_supply/BAT0/energy_now").read().strip())
        charge_full = int(
            open("/sys/class/power_supply/BAT0/energy_full").read().strip()
        )
        power_now = int(open("/sys/class/power_supply/BAT0/power_now").read().strip())

        if charge_now == 0 or charge_full == 0 or power_now == 0:
            return None
        if self.is_charging():
            time_remaining = (charge_full - charge_now) / power_now
        else:
            time_remaining = charge_now / power_now
        return time_remaining * 60

    def get_battery_info(self):
        """Retrieve detailed battery information.

        Returns:
            dict: Dictionary containing battery percentage, charging status, and time remaining.
        """
        return {
            "percentage": self.get_percentage(),
            "is_charging": self.is_charging(),
            "time_remaining": self.get_time_remaining(),
        }
