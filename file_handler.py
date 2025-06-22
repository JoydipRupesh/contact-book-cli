# file_handler.py

import csv
import os

FILENAME = "contacts.csv"

def load_contacts():
    contacts = []
    if os.path.exists(FILENAME):
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    return contacts

def save_contacts(contacts):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ['Name', 'Phone', 'Email', 'Address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)
