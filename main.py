# main.py
from smartphone import Smartphone  # Import Smartphone class
from laptop import Laptop  # Import Laptop class
from tablet import Tablet  # Import Tablet class
from cart import Cart  # Import Cart class


def show_devices(devices):
    for i, device in enumerate(devices):
        print(f"{i + 1}. {device}")


def main():
    # Example devices
    devices = [
        Smartphone("iPhone 13", 999, 10, 12, 6.1, 20),
        Laptop("MacBook Pro", 2499, 5, 24, 16, 3.1),
        Tablet("iPad Pro", 799, 8, 12, "2732x2048", 500)
    ]

    cart = Cart()

    while True:
        print("\nMenu:")
        print("1. Show Devices")
        print("2. Show Cart")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_devices(devices)
            device_choice = int(input("Choose a device to add to the cart (1, 2, etc.): ")) - 1
            amount = int(input("Enter the quantity: "))
            cart.add_device(devices[device_choice], amount)

        elif choice == "2":
            cart.print_items()
            print(f"Total Price: ${cart.get_total_price()}")

        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
