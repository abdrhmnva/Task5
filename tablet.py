# tablet.py
from device import Device  # Import Device class

class Tablet(Device):
    def __init__(self, name, price, stock, warranty, screen_resolution, weight):
        super().__init__(name, price, stock, warranty)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return f"{super().__str__()}, Screen Resolution: {self.screen_resolution}, Weight: {self.weight}g"

    def browse_internet(self):
        return f"Browsing the internet on {self.name}"

    def use_touchscreen(self):
        return f"Using the touchscreen on {self.name}"

