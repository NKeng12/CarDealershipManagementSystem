from collections import deque

import colorama

colorama.init()
customer_database = ["S111", "S222", "S33"]


class Car:
    def __init__(self, car_engine_no, car_brand, car_type, mileage, reg_year):
        self.car_engine_no = car_engine_no
        self.car_brand = car_brand
        self.car_type = car_type
        self.mileage = mileage
        self.reg_year = reg_year


class CustomerRequest:
    def __init__(self, customer_id, details):
        self.customer_id = customer_id
        self.details = details
        self.email = None  # Initialize the email attribute to None
        self.tier = None  # Initialize the tier attribute to None
        self.points = None  # Initialize the points attribute to None

# Option 7
class CustomerRequestQueue:
    def __init__(self):
        self.customer_requests = deque()

    def is_valid_request(self, customer_id, details):
        # Check if the customer ID exists in the customer_database
        if customer_id not in customer_database:
            print(colorama.Fore.RED + "Invalid Customer ID. Customer ID does not exist in the database.")
            return False

        # Add other validation checks here (e.g., details length, etc.)
        if not customer_id:
            print(colorama.Fore.RED + "Invalid Customer ID. Please provide a valid Customer ID.")
            return False
        if not details or len(details) < 10:
            print(colorama.Fore.RED + "Invalid Details. Please provide details with a minimum of 10 characters.")
            return False

        return True

    # CR menu Option 1
    def add_customer_request(self, customer_id, details):
        if not self.is_valid_request(customer_id, details):
            return

        # Sequential Search validation to check if the customer request already exists
        if any(request.customer_id == customer_id for request in self.customer_requests):
            print(colorama.Fore.RED + "Customer request already exists.")
        else:
            request = CustomerRequest(customer_id, details)
            self.customer_requests.append(request)
            print(
                colorama.Fore.GREEN + f"Customer request added successfully. Queue Number: {len(self.customer_requests)}")

            # Set the attributes for the customer request right after adding it to the queue
            if customer_id == 'S111':
                request.email = "customer1@example.com"
                request.tier = "A"
                request.points = 100
            elif customer_id == 'S222':
                request.email = "customer2@example.com"
                request.tier = "B"
                request.points = 50
            elif customer_id == 'S33':
                request.email = "customer3@example.com"
                request.tier = "C"
                request.points = 20

    # CR menu Option 2
    def view_num_customer_requests(self):
        num_requests = len(self.customer_requests)
        print(colorama.Fore.YELLOW + f"Number of Customer Requests in Queue: {num_requests}")

    # CR menu Option 3
    def process_next_customer_request(self):
        if not self.customer_requests:
            print(colorama.Fore.RED + "No customer requests in the Queue.")
            return

        request = self.customer_requests.popleft()
        print(colorama.Fore.YELLOW + "Processing Customer Request:")
        print(colorama.Fore.CYAN + f"Queue Number: {len(self.customer_requests) + 1}")
        print(colorama.Fore.CYAN + f"Customer ID: {request.customer_id}")
        print(colorama.Fore.CYAN + f"Details: {request.details}")
        print(colorama.Fore.CYAN + f"Email: {request.email}")
        print(colorama.Fore.CYAN + f"Tier: {request.tier}")
        print(colorama.Fore.CYAN + f"Points: {request.points}")
        self.view_num_customer_requests()

    # CR menu Option 4
    def search_by_customer_id(self, customer_id):
        found_requests = []
        for request in self.customer_requests:
            if request.customer_id == customer_id:
                found_requests.append(request)

        if found_requests:
            print(colorama.Fore.GREEN + f"Found {len(found_requests)} requests with Customer ID '{customer_id}':")
            for found_request in found_requests:
                print(colorama.Fore.CYAN + f"Queue Number: {self.customer_requests.index(found_request) + 1}")
                print(colorama.Fore.CYAN + f"Customer ID: {found_request.customer_id}")
                print(colorama.Fore.CYAN + f"Details: {found_request.details}")
                print(colorama.Fore.CYAN + f"Email: {found_request.email}")
                print(colorama.Fore.CYAN + f"Tier: {found_request.tier}")
                print(colorama.Fore.CYAN + f"Points: {found_request.points}")
                print("-" * 30)
        else:
            print(colorama.Fore.RED + f"No requests found with Customer ID '{customer_id}'.")

    # CR menu Option 5
    def remove_customer_request(self, customer_id):
        removed_requests = [request for request in self.customer_requests if request.customer_id == customer_id]

        if removed_requests:
            for request in removed_requests:
                self.customer_requests.remove(request)
            print(
                colorama.Fore.GREEN + f"Successfully removed {len(removed_requests)} requests with Customer ID '{customer_id}'.")
        else:
            print(colorama.Fore.RED + f"No requests found with Customer ID '{customer_id}'.")

    # CR menu Option 6
    def edit_customer_request(self, customer_id, new_details):
        for request in self.customer_requests:
            if request.customer_id == customer_id:
                request.details = new_details
                print(colorama.Fore.GREEN + f"Details for Customer ID {customer_id} updated successfully.")
                break
        else:
            print(colorama.Fore.RED + f"Customer ID: {customer_id} not found in the queue.")

# Create an instance of CustomerRequestQueue
queue = CustomerRequestQueue()

for request in queue.customer_requests:
    if request.customer_id == 'S111':
        request.email = "customer1@example.com"
        request.tier = "A"
        request.points = 100
    elif request.customer_id == 'S222':
        request.email = "customer2@example.com"
        request.tier = "B"
        request.points = 50
    elif request.customer_id == 'S333':
        request.email = "customer3@example.com"
        request.tier = "C"
        request.points = 20


class CarDealer:
    def __init__(self):
        self.cars = []
        self.data_populated = False
        self.customer_requests = deque()  # Queue to store customer requests

    # Option 1
    def display_all_cars(self):
        if not self.cars:
            print(colorama.Fore.RED + "No cars found.")
        else:
            for car in self.cars:
                self.display_car_details(car)

        
    def display_car_details(self, car):
        print("\n")
        print(colorama.Fore.CYAN + "Car Engine No:", car.car_engine_no)
        print(colorama.Fore.CYAN + "Car Brand:", car.car_brand)
        print(colorama.Fore.CYAN + "Car Type:", car.car_type)
        print(colorama.Fore.CYAN + "Mileage:", car.mileage)
        print(colorama.Fore.CYAN + "Registration Year:", car.reg_year)
        print()

    # Option 2
    def add_car(self):

        # Ensures car engine number is 12 digits long and unique
        while True:
            try:
                car_engine_no = input(colorama.Fore.CYAN + "Enter Car Engine No: ")
                if len(car_engine_no) == 12 and car_engine_no.isdigit():
                    if any(car.car_engine_no == car_engine_no for car in self.cars):
                        print(
                            colorama.Fore.RED + "Car with the same engine number already exists. Please enter a unique engine number.")
                    else:
                        break
                else:
                    print(colorama.Fore.RED + "Engine number has to be 12 digits long and consist of only digits.")
            except ValueError:
                print(colorama.Fore.RED + "Invalid input. Please enter a valid integer for Mileage.")

        # Ensures car brand is alphabetical
        while True:
            car_brand = input(colorama.Fore.CYAN + "Enter Car Brand: ")
            if car_brand.isalpha():
                break
            else:
                print(colorama.Fore.RED + "Invalid Car Brand. Please enter alphabetic characters only.")

        # Ensures car type is alphanumerical
        while True:
            car_type = input(colorama.Fore.CYAN + "Enter Car Type: ")
            if car_type.isalnum():
                break
            else:
                print(colorama.Fore.RED + "Invalid Car Type. Please enter alphanumeric characters only.")

        # Ensures mileage is not less an 0
        while True:
            try:
                mileage = int(input(colorama.Fore.CYAN + "Enter Mileage: "))
                if mileage >= 0:
                    break
                else:
                    print(colorama.Fore.RED + "Mileage cannot be negative. Please enter a non-negative value.")
            except ValueError:
                print(colorama.Fore.RED + "Invalid input. Please enter a valid integer for Mileage.")

        # Ensures registration year is between 1990 and 2023
        while True:
            try:
                reg_year = int(input(colorama.Fore.CYAN + "Enter Registration Year: "))
                current_year = 2023
                if 1900 <= reg_year <= current_year:
                    break
                else:
                    print(colorama.Fore.RED + f"Registration Year must be between 1900 and {current_year}.")
            except ValueError:
                print(colorama.Fore.RED + "Invalid input. Please enter a valid integer for Registration Year.")

        car = Car(car_engine_no, car_brand, car_type, mileage, reg_year)
        self.cars.append(car)
        print(colorama.Fore.GREEN + "Car added successfully.")

    # Option 3
    def bubble_sort_car_brand(self):
        n = len(self.cars)

        for i in range(n - 1, 0, -1):
            for j in range(i):
                if self.cars[j].car_brand > self.cars[j + 1].car_brand:
                    self.cars[j], self.cars[j + 1] = self.cars[j + 1], self.cars[j]

    # Option 4
    def insertion_sort_mileage(self):
        n = len(self.cars)

        for i in range(1, n):
            value = self.cars[i]
            pos = i

            while pos > 0 and value.mileage > self.cars[pos - 1].mileage:
                self.cars[pos] = self.cars[pos - 1]
                pos -= 1

            self.cars[pos] = value

        # Option 5
    def selection_sort_car_type(self):
        n = len(self.cars)

        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                if self.cars[j].car_type < self.cars[min_index].car_type:
                    min_index = j

            self.cars[i], self.cars[min_index] = self.cars[min_index], self.cars[i]

    # Option 6
    def merge_sort(self, cars):
        if len(cars) <= 1:
            return cars

        middle = len(cars) // 2
        left_half = cars[:middle]
        right_half = cars[middle:]

        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)

        return self.merge(left_half, right_half)

    # Option 6 part 2
    def merge(self, left, right):
        merged_list = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index].reg_year < right[right_index].reg_year or (
                    left[left_index].reg_year == right[right_index].reg_year and
                    left[left_index].car_engine_no < right[right_index].car_engine_no
            ):
                merged_list.append(left[left_index])
                left_index += 1
            else:
                merged_list.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            merged_list.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged_list.append(right[right_index])
            right_index += 1

        return merged_list
    
    # Option 8
    def populate_data(self):
        if not self.data_populated:
            cars_data = [
                (617572248460, "BMW", "LUXURY", 21835, 2000),
                (455816187746, "Mercedes", "CONVERTIBLE", 79931, 2007),
                (192841491966, "Toyota", "HYBRID", 57001, 2010),
                (701001166935, "Honda", "MINIVAN", 82741, 1999),
                (427524730918, "Mazda", "SUV", 90529, 2012),
                (101816051527, "Nissan", "SEDAN", 40526, 2015),
                (101816051528, "Nissan", "SEDAN", 40526, 2010),
                (101816051537, "Nissan", "SEDAN", 40526, 2010),
                (101816051538, "Nissan", "SEDAN", 40526, 2010),
            ]

            for car_data in cars_data:
                car_engine_no, car_brand, car_type, mileage, reg_year = car_data
                car = Car(car_engine_no, car_brand, car_type, mileage, reg_year)
                self.cars.append(car)

            self.data_populated = True
            print(colorama.Fore.GREEN + "Data populated successfully.")
        else:
            print(colorama.Fore.RED + "Data has already been populated.")

    # Option 9
    def edit_car(self):
        engine_no = input(colorama.Fore.CYAN + "Enter the Engine No. of the car to edit: ")
        for car in self.cars:
            if car.car_engine_no == engine_no:
                print(colorama.Fore.YELLOW + "Enter new details for the car:")
                car_brand = input(colorama.Fore.CYAN + "Car Brand: ")
                car_type = input(colorama.Fore.CYAN + "Car Type: ")
                mileage = int(input(colorama.Fore.CYAN + "Mileage: "))
                reg_year = int(input(colorama.Fore.CYAN + "Registration Year: "))
                car.car_brand = car_brand
                car.car_type = car_type
                car.mileage = mileage
                car.reg_year = reg_year
                print(colorama.Fore.GREEN + "Car details updated successfully.")
                return
        print(colorama.Fore.RED + "Car not found.")

    # Option 10
    def delete_car(self):
        engine_no = input(colorama.Fore.CYAN + "Enter the Engine No. of the car to delete: ")
        for car in self.cars:
            if car.car_engine_no == engine_no:
                self.cars.remove(car)
                print(colorama.Fore.GREEN + "Car deleted successfully.")
                return
        print(colorama.Fore.RED + "Car not found.")

    # Option 11
    def display_car_statistics(self):
        if not self.cars:
            print(colorama.Fore.RED + "No cars found.")
            return

        total_cars = len(self.cars)
        total_mileage = sum(car.mileage for car in self.cars)
        average_mileage = total_mileage / total_cars if total_cars > 0 else 0

        brand_counts = {}
        for car in self.cars:
            brand_counts[car.car_brand] = brand_counts.get(car.car_brand, 0) + 1

        most_common_brand = max(brand_counts, key=brand_counts.get)
        brand_percentage = (brand_counts[most_common_brand] / total_cars) * 100

        print(colorama.Fore.YELLOW + "Car Statistics:")
        print(colorama.Fore.CYAN + "Total Cars:", total_cars)
        print(colorama.Fore.CYAN + "Total Mileage:", total_mileage)
        print(colorama.Fore.CYAN + "Average Mileage:", average_mileage)
        print(colorama.Fore.CYAN + "Most Common Brand:", most_common_brand)
        print(colorama.Fore.CYAN + "Brand Percentage:", brand_percentage)

    # Option 12
    def search_by_brand(self, brand):
        matching_cars = [car for car in self.cars if car.car_brand.lower() == brand.lower()]

        if matching_cars:
            print(colorama.Fore.YELLOW + "Matching Cars:")
            for car in matching_cars:
                self.display_car_details(car)
        else:
            print(colorama.Fore.CYAN + "No cars found with the specified brand.")

    # Option 13
    def search_by_mileage_range(self, min_mileage, max_mileage):
        matching_cars = [car for car in self.cars if min_mileage <= car.mileage <= max_mileage]

        if matching_cars:
            print(colorama.Fore.YELLOW + "Matching Cars:")
            for car in matching_cars:
                self.display_car_details(car)
        else:
            print(colorama.Fore.CYAN + "No cars found within the specified mileage range.")

    # Option 14
    def search_by_registration_year_range(self, min_year, max_year):
        matching_cars = [car for car in self.cars if min_year <= car.reg_year <= max_year]

        if matching_cars:
            print(colorama.Fore.YELLOW + "Matching Cars:")
            for car in matching_cars:
                self.display_car_details(car)
        else:
            print(colorama.Fore.CYAN + "No cars found within the specified registration year range.")


# Menu
def display_menu():
    print()
    print(colorama.Fore.YELLOW + "SINGCAR USED CAR DEALER")
    print(colorama.Fore.CYAN + "1. " + colorama.Fore.CYAN + "Display all cars' records")
    print(colorama.Fore.CYAN + "2. " + colorama.Fore.CYAN + "Add a new car record")
    print(colorama.Fore.CYAN + "3. " + colorama.Fore.CYAN + "Sort cars by Car Brand (Ascending Order)")
    print(colorama.Fore.CYAN + "4. " + colorama.Fore.CYAN + "Sort cars by Mileage (Descending Order)")
    print(colorama.Fore.CYAN + "5. " + colorama.Fore.CYAN + "Sort cars by Car Type (Ascending Order)")
    print(colorama.Fore.CYAN + "6. " + colorama.Fore.CYAN + "Sort cars by Registration Year and Car Engine Number (Ascending Order)")
    print(colorama.Fore.CYAN + "7. " + colorama.Fore.CYAN + "Manage customer requests")
    print(colorama.Fore.CYAN + "8. " + colorama.Fore.CYAN + "Populate data")
    print(colorama.Fore.CYAN + "9. " + colorama.Fore.MAGENTA + "Edit a car record")
    print(colorama.Fore.CYAN + "10. " + colorama.Fore.MAGENTA + "Delete a car record")
    print(colorama.Fore.CYAN + "11. " + colorama.Fore.MAGENTA + "Display car statistics")
    print(colorama.Fore.CYAN + "12. " + colorama.Fore.MAGENTA + "Search cars by Car Brand")
    print(colorama.Fore.CYAN + "13. " + colorama.Fore.MAGENTA + "Search cars by Mileage Range")
    print(colorama.Fore.CYAN + "14. " + colorama.Fore.MAGENTA + "Search cars by Registration Year Range")
    print(colorama.Fore.CYAN + "15. " + colorama.Fore.RED + "EXIT")
    print(colorama.Style.RESET_ALL)


def main():
    queue = CustomerRequestQueue()  # Create an instance of CustomerRequestQueue to manage customer requests

    car_dealer = CarDealer()

    while True:
        display_menu()
        choice = input(colorama.Fore.YELLOW + "Enter your choice: ")

        if choice == '1':
            car_dealer.display_all_cars()
        elif choice == '2':
            car_dealer.add_car()
        elif choice == '3':
            car_dealer.bubble_sort_car_brand()
            car_dealer.display_all_cars()  # Display sorted cars
        elif choice == '4':
            car_dealer.insertion_sort_mileage()
            car_dealer.display_all_cars()  # Display sorted cars
        elif choice == '5':
            car_dealer.selection_sort_car_type()
            car_dealer.display_all_cars()
        elif choice == '6':
            sorted_cars = car_dealer.merge_sort(car_dealer.cars)
            car_dealer.cars = sorted_cars
            car_dealer.display_all_cars()
        elif choice == '7':
            print(colorama.Fore.MAGENTA + "\n========= Customer Request Menu =========")
            print(colorama.Fore.CYAN + "1. Add Customer Request")
            print(colorama.Fore.CYAN + "2. View Number of Customer Requests")
            print(colorama.Fore.CYAN + "3. Service next Customer Request")
            print(colorama.Fore.CYAN + "4. " + colorama.Fore.MAGENTA + "Search Customer Request by Customer ID")
            print(colorama.Fore.CYAN + "5. " + colorama.Fore.MAGENTA + "Remove Customer Request")
            print(colorama.Fore.CYAN + "6. " + colorama.Fore.MAGENTA + "Edit Customer Request")
            print(colorama.Fore.CYAN + "0. " + colorama.Fore.RED + "Return to Main Menu")
            print(colorama.Fore.MAGENTA + f"=========================================\n")

            sub_choice = int(input(colorama.Fore.CYAN + "Enter your choice: "))

            if sub_choice == 1:
                customer_id = input(colorama.Fore.CYAN + "Enter Customer ID for the request: ")
                if customer_id in customer_database:  # Check if the customer ID exists in the database
                    details = input(colorama.Fore.CYAN + "Enter Details for the request: ")
                    queue.add_customer_request(customer_id, details)
                else:
                    print(colorama.Fore.RED + "Invalid Customer ID. Customer ID does not exist in the database.")
            elif sub_choice == 2:
                queue.view_num_customer_requests()
            elif sub_choice == 3:
                queue.process_next_customer_request()
            elif sub_choice == 4:
                customer_id = input(colorama.Fore.CYAN + "Enter Customer ID to search: ")
                queue.search_by_customer_id(customer_id)
            elif sub_choice == 5:
                customer_id = input(colorama.Fore.CYAN + "Enter Customer ID to remove: ")
                queue.remove_customer_request(customer_id)
            elif sub_choice == 6:
                customer_id = input(colorama.Fore.CYAN + "Enter Customer ID for the request you want to edit: ")
                new_details = input(colorama.Fore.CYAN + "Enter the new details for the customer request: ")
                queue.edit_customer_request(customer_id, new_details)
            else:
                print(colorama.Fore.RED + "Invalid choice. Please try again.")

        elif choice == '8':
            car_dealer.populate_data()
        elif choice == '9':
            car_dealer.edit_car()
        elif choice == '10':
            car_dealer.delete_car()
        elif choice == '11':
            car_dealer.display_car_statistics()
        elif choice == '12':
            brand = input(colorama.Fore.CYAN + "Enter the car brand: ")
            car_dealer.search_by_brand(brand)
        elif choice == '13':
            min_mileage = int(input(colorama.Fore.CYAN + "Enter the minimum mileage: "))
            max_mileage = int(input(colorama.Fore.CYAN + "Enter the maximum mileage: "))
            car_dealer.search_by_mileage_range(min_mileage, max_mileage)
        elif choice == '14':
            min_year = int(input(colorama.Fore.CYAN + "Enter the minimum registration year: "))
            max_year = int(input(colorama.Fore.CYAN + "Enter the maximum registration year: "))
            car_dealer.search_by_registration_year_range(min_year, max_year)


        elif choice == '15':
            print(colorama.Fore.GREEN + "Exiting the program.")
            break
        else:
            print(colorama.Fore.RED + "Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
