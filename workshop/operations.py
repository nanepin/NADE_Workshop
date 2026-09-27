from .data import customers, computers, repair_jobs, parts, diagnosis, status
from .storage import save_customer, save_computer, save_job, save_part

def add_customer():
    name = input("Enter customer's name: ").strip()
    customer_id = input("Enter customer id: ").strip()
    phone = input("Enter phone number: ").strip()

    if any(person["id"].lower() == customer_id.lower() for person in customers):
        print("Customer is already registered.")
        return
    
    customers.append({
        "id": customer_id,
        "name": name,
        "phone": phone
    })
    save_customer()
    print("Customer added successfully.")
    return
    
    
def view_customer():
    for customer in customers:
        print("ID: ", customer["id"])
        print("Name: ", customer["name"])
        print("Phone: ", customer["phone"])
        print("--------------------------")
    
def search_customer():
    print("1. Search by ID")
    print("2. Search by name")
    print("3. Search by Phone")
    try: 

        choice = int(input("Choose from above: "))

        if choice == 1:
            customer_id = input("Enter customer's ID: ").strip()
            for customer in customers:
                if customer["id"].lower() == customer_id.lower():
                    print(customer)
                    return

            print("Customer not found.")

        elif choice == 2:
            customer_name = input("Enter customer's name: ").strip()
            for customer in customers:
                if customer["name"].lower() == customer_name.lower():
                    print(customer)
                    return

            print("Customer not found.")
            
        elif choice == 3:
            customer_phone = input("Enter customer's phone number: ").strip()
            for customer in customers:
                if customer["phone"] == customer_phone:
                    print(customer)
                    return
                
            print("Customer not found.")

        else:
            print("Invalid.")

    except ValueError:
        print("Invalid.")
        
    
def remove_customer():
    customer_id = input("Enter ID: ").strip()
    for customer in customers:
        if customer["id"].lower() == customer_id.lower():
            customers.remove(customer)
            save_customer()
            print("Removed successfully.")
            return
        
    print("Could not remove customer. Such as customer with", customer_id, "was never registered.")

def register_pc():
    name = input("Enter computer's name: ").strip()
    comp_id = input("Enter computer's ID: ").strip()
    customer = input("Enter customer's ID: ").strip()
    problem = input("Specify the problem: ").strip()

    if any(pc["id"].lower() == comp_id.lower() for pc in computers):
        print("PC ID is already registered.")
        return

    for person in customers:
        if person["id"].lower() == customer.lower():
            computers.append({
                "name": name,
                "id": comp_id,
                "customer": customer,
                "issue": problem
            })
            save_computer()
            print("Added successfully.")
            break
        
    print("Get the customer registered first.")
        
        
def view_pc():
    for pc in computers:
        print("Name: ", pc["name"])
        print("ID: ", pc["id"])
        print("Customer: ", pc["customer"])
        print("Problem: ", pc["issue"])
        print("----------------------")
        
    
def search_pc():
    pc_id = input("Enter PC's ID: ").strip()
    for pc in computers:
        if pc["id"].lower() == pc_id.lower():
            print(pc)
            return

    print("PC not found.")

def remove_pc():
    pc_id = input("Enter PC's id: ").strip()
    for pc in computers:
        if pc["id"].lower() == pc_id.lower():
            computers.remove(pc)
            save_computer()
            print("Successfully removed the PC.")
            return

    print("Could not remove the PC. Such a PC", pc_id, "does not exist.")
        
def create_job():
    pc0 = input("Enter PC's ID: ").strip()

    if any(job["pc"].lower() == pc0 for job in repair_jobs):
        print("A job is already associated with that PC ID.")
        return
    
    for pc in computers:
        if pc["id"].lower() == pc0.lower():
            customer = pc["customer"]
            repair_jobs.append({
                "pc": pc0,
                "customer": customer,
                "diagnosis": diagnosis[0],
                "status": status[0],
                "parts": [],
                "cost": 0
            })
            print("Job added successfully.")
            save_job()
            return
            break

    print("Job was not created. PC is not registered.")


def view_job():
    for job in repair_jobs:
        print("PC: ", job["pc"])
        print("Diagnosis: ", job["diagnosis"])
        print("Status: ", job["status"])
        print("Parts: ", job["parts"])
        print("Cost: ", job["cost"])
        print("-----------------")
        

def update_diagnosis():
    pc = input("Enter PC's ID: ").strip()
    for job in repair_jobs:
        if job["pc"].lower() == pc.lower():
            job["diagnosis"] = diagnosis[1]
            save_job()
            print("Diagnosis updated successfully.")
            return

    print("Diagnosis could not be updated. Repair job for specified PC ID does not exist.")

def update_status():
    pc = input("Enter PC's ID: ").strip()
    for job in repair_jobs:
        if job["pc"].lower() == pc.lower():
            if job["diagnosis"] == diagnosis[1]:
                job["status"] = status[1]
                save_job()
                print("Status updated successfully.")
                return
            
    print("Status could not be updated. Job not assined to specified PC.")

def remove_job():
    pc = input("Enter PC's ID: ").strip()
    for job in repair_jobs:
        if job["pc"].lower() == pc.lower():
            if job["status"] == status[1]:
                repair_jobs.remove(job)
                save_job()
                print("Successfully removed the job.")
                return
            
    print("Job could not be removed. Its either not complete or specified PC ID does not have a repair job registered.")

def add_part_to_repair():
    part0 = input("Enter part name: ").strip()
    pc = input("Enter PC ID: ").strip()
    for part in parts:
        if part["name"].lower() == part0.lower():
            for job in repair_jobs:
                if job["pc"].lower() == pc.lower():
                    job["parts"].append(part)
                    save_job()
                    print("Successfully added part to repair job.")
                    return
                
    print("Either PC is not registered or specified part is not inside inventory. Contact the manager.")

def calculate_cost():
    pc = input("Enter PC's ID: ").strip()
    for job in repair_jobs:
        if job["pc"].lower() == pc.lower():
            total = 0
            for part in job["parts"]:
                total = part["price"] + total

            job["cost"] = total
            print(total)
            return total

def add_part_to_inventory():
    try:
        name = input("Enter part's name: ").strip()
        price = int(input("Enter price of the part: "))
        parts.append({
            "name": name,
            "price": price
        })
        save_part()
        print("Successfully added part to inventory.")
        return
    
    except ValueError:
        print("Please enter in digits.")

def view_inventory():
    for part in parts:
        print("Name: ", part["name"])
        print("Price: ", part["price"])
        print("----------------------")

def search_part():
    name = input("Enter part's name: ").strip()
    for part in parts:
        if part["name"].lower() == name.lower():
            print(part)
            return

def update_price():
    try: 
        name = input("Enter part's name: ").strip()
        price = int(input("Enter new price: "))
        for part in parts:
            if part["name"].lower() == name.lower():
                part["price"] = price
                save_part()
                print("Price updated successfully.")
                return

        print("Price couldnt be updated. Part does not exist. Register the part first.")

    except ValueError:
        print("Please enter in digits.")
