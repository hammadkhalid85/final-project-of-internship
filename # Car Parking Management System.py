# Car Parking Management System

class ParkingSystem:
    def __init__(self, total_slots, password):
        self.total_slots = total_slots      # Total slots in parking
        self.available_slots = total_slots  # Slots currently free
        self.cars = {}                      # Dictionary to store car details
        self.password = password            # Security password for admin
        self.parking_rate = 50              # Per hour rate (can change)

    def admin_login(self):
        pwd = input("Enter Admin Password: ")
        if pwd == self.password:
            print("✅ Admin Login Successful!\n")
            return True
        else:
            print("❌ Wrong Password! Access Denied.")
            return False

    def park_car(self):
        if self.available_slots > 0:
            plate = input("Enter Car Plate Number: ")
            owner = input("Enter Owner Name: ")
            hours = int(input("Enter Parking Hours: "))
            cost = hours * self.parking_rate

            self.cars[plate] = {"owner": owner, "hours": hours, "cost": cost}
            self.available_slots -= 1

            print(f"✅ Car {plate} parked successfully!")
            print(f"Parking Cost: Rs {cost}")
            print(f"Available Slots: {self.available_slots}/{self.total_slots}\n")
        else:
            print("❌ No slots available!\n")

    def remove_car(self):
        plate = input("Enter Car Plate Number to Remove: ")
        if plate in self.cars:
            del self.cars[plate]
            self.available_slots += 1
            print(f"✅ Car {plate} removed successfully!")
            print(f"Available Slots: {self.available_slots}/{self.total_slots}\n")
        else:
            print("❌ Car not found!\n")

    def view_parked_cars(self):
        if self.cars:
            print("\n🚗 Parked Cars Details:")
            for plate, info in self.cars.items():
                print(f"Plate: {plate}, Owner: {info['owner']}, Hours: {info['hours']}, Cost: Rs {info['cost']}")
            print()
        else:
            print("No cars are parked currently.\n")

    def update_car_info(self):
        plate = input("Enter Car Plate Number to Update: ")
        if plate in self.cars:
            new_hours = int(input("Enter New Parking Hours: "))
            new_cost = new_hours * self.parking_rate
            self.cars[plate]["hours"] = new_hours
            self.cars[plate]["cost"] = new_cost
            print(f"✅ Car {plate} updated successfully!\n")
        else:
            print("❌ Car not found!\n")

    def show_menu(self):
        while True:
            print("\n===== Car Parking Management System =====")
            print("1. Park a Car")
            print("2. Remove a Car")
            print("3. View Parked Cars")
            print("4. Update Car Parking Hours")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.park_car()
            elif choice == "2":
                self.remove_car()
            elif choice == "3":
                self.view_parked_cars()
            elif choice == "4":
                self.update_car_info()
            elif choice == "5":
                print("Exiting... Thank you!")
                break
            else:
                print("❌ Invalid choice! Please try again.\n")


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    print("==== Welcome to Car Parking Management System ====")
    total_slots = int(input("Enter total parking slots: "))
    admin_password = input("Set Admin Password: ")

    parking_system = ParkingSystem(total_slots, admin_password)

    if parking_system.admin_login():
        parking_system.show_menu()
