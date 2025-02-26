# laptop.py
from device import Device  # Import Device class

class Laptop(Device):
    def __init__(self, name, price, stock, warranty, ram_size, processor_speed):
        # Pass the correct arguments to the parent class
        super().__init__(name, price, stock, warranty)  # This is the correct way to call the parent constructor
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return f"{super().__str__()}, RAM: {self.ram_size} GB, Processor: {self.processor_speed} GHz"

    def run_program(self, program_name):
        return f"Running {program_name} on {self.name}"

    def use_keyboard(self):
        return f"Typing on the {self.name}'s keyboard"
