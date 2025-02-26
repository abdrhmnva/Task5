# cart.py
class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            device.reduce_stock(amount)
        else:
            print(f"Not enough stock for {device.name}")

    def remove_device(self, device, amount):
        for i, (dev, amt) in enumerate(self.items):
            if dev == device and amt >= amount:
                self.items[i] = (dev, amt - amount)
                self.total_price -= dev.price * amount
                return
        print(f"Device {device.name} not found or not enough quantity to remove")

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        for device, amount in self.items:
            print(f"{device.name}: {amount} units, Total: ${device.price * amount}")

    def checkout(self):
        print("Proceeding to checkout:")
        self.print_items()
        print(f"Total Price: ${self.get_total_price()}")
