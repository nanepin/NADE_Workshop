from . import operations
from . import storage

def main_menu():
    print("Welcome to NADE's Computer Workshop Manager")
    print()
    while True:
        print("Choose one of the following:")
        print()
        print("1. Customers")
        print("2. Computers")
        print("3. Repair Jobs")
        print("4. Parts")
        print("5. Exit")
        print()

        try:
            choice = int(input("Choose from above: "))

            if choice == 1:
                while True:
                    try:
                        print("1. Add a customer")
                        print("2. View all customers")
                        print("3. Search for a customer")
                        print("4. Remove a customer")
                        print("5. Exit")

                        choice = int(input("Choose from above: "))

                        if choice == 1:
                            operations.add_customer()

                        elif choice == 2:
                            operations.view_customer()

                        elif choice == 3:
                            operations.search_customer()

                        elif choice == 4:
                            operations.remove_customer()

                        elif choice == 5:
                            break

                        else:
                            print("Invalid option.")
                                
                    except ValueError:
                        print("Invalid.")

            elif choice == 2:
                while True:
                    try:
                        print("1. Add a computer")
                        print("2. View all computers")
                        print("3. Search for a computer")
                        print("4. Remove a computer")
                        print("5. Exit")

                        choice = int(input("Choose from above: "))

                        if choice == 1:
                            operations.register_pc()
                            
                        elif choice == 2:
                            operations.view_pc()

                        elif choice == 3:
                            operations.search_pc()

                        elif choice == 4:
                            operations.remove_pc()

                        elif choice == 5:
                            break

                        else:
                            print("Invalid option.")

                    except ValueError:
                        print("Invalid.")

            elif choice == 3:
                print("This is for the employees only.")
                print()
                while True:
                    try: 
                        print("1. Create a job")
                        print("2. View all jobs")
                        print("3. Update a job's diagnosis")
                        print("4. Update a job's status")
                        print("5. Remove a job")
                        print("6. Add a part to job")
                        print("7. Calculate all cost of a job")
                        print("8. Exit")

                        choice = int(input("Choose from above: "))

                        if choice == 1:
                            operations.create_job()

                        elif choice == 2:
                            operations.view_job()

                        elif choice == 3:
                            operations.update_diagnosis()

                        elif choice == 4:
                            operations.update_status()

                        elif choice == 5:
                            operations.remove_job()

                        elif choice == 6:
                            operations.add_part_to_repair()

                        elif choice == 7:
                            operations.calculate_cost()

                        elif choice == 8:
                            break

                        else:
                            print("Invalid option.")

                    except ValueError:
                        print("Invalid.")

            elif choice == 4:
                print("This is for the employees only.")
                print()
                while True:
                    try:
                        print("1. Add a new part to inventory")
                        print("2. View all parts of inventory")
                        print("3. Search for a part from inventory")
                        print("4. Update price of a part")
                        print("5. Exit")

                        choice = int(input("Choose from above: "))

                        if choice == 1:
                            operations.add_part_to_inventory()

                        elif choice == 2:
                            operations.view_inventory()

                        elif choice == 3:
                            operations.search_part()

                        elif choice == 4:
                            operations.update_price()

                        elif choice == 5:
                            break

                        else:
                            print("Invalid option.")

                    except ValueError:
                        print("Invalid.")

            elif choice == 5:
                storage.save_customer()
                storage.save_computer()
                storage.save_job()
                storage.save_part()
                break

            else:
                print("Invalid option.")

        except ValueError:
                print("Invalid.")

