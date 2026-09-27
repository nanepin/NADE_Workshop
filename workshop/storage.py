import json
from . import data

def load_all_data():
    with open("workshop/storage/customers.json", "r") as file:
        data.customers[:] = json.load(file)

    with open("workshop/storage/computers.json", "r") as file:
        data.computers[:] = json.load(file)

    with open("workshop/storage/repair_jobs.json", "r") as file:
        data.repair_jobs[:] = json.load(file)

    with open("workshop/storage/parts.json", "r") as file:
        data.parts[:] = json.load(file)

def save_customer():
    with open("workshop/storage/customers.json", "w") as file:
        json.dump(data.customers, file, indent=4)

def save_computer():
    with open("workshop/storage/computers.json", "w") as file:
        json.dump(data.computers, file, indent=4)

def save_job():
    with open("workshop/storage/repair_jobs.json", "w") as file:
        json.dump(data.repair_jobs, file, indent=4)

def save_part():
    with open("workshop/storage/parts.json", "w") as file:
        json.dump(data.parts, file, indent=4)
