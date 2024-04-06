class GarbageManagementSystem:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_capacity = 0

    def add_garbage(self, amount):
        self.current_capacity += amount
        self.check_status()

    def check_status(self):
        percentage_full = (self.current_capacity / self.max_capacity) * 100

        if percentage_full >= 95:
            self.notify("red")
        else:
            self.notify("no color")

    def notify(self, color):
        print("Garbage level:", color)

# Example usage:
if __name__ == "__main__":
    garbage_system = GarbageManagementSystem(max_capacity=1000)  # Set maximum capacity
    garbage_system.add_garbage(500)  # Add some garbage
    garbage_system.add_garbage(300)  # Add some more garbage
    garbage_system.add_garbage(250)  # Add even more garbage
