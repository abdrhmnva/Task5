# smartphone.py
from device import Device  # Import Device class

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty, screen_size, battery_life):
        super().__init__(name, price, stock, warranty)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return f"{super().__str__()}, Screen Size: {self.screen_size}\" , Battery Life: {self.battery_life} hrs"

    def make_call(self):
        return f"Making a call from {self.name}"

    def install_app(self, app_name):
        return f"Installing {app_name} on {self.name}"
