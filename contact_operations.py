# contact_operations.py

from file_handler import load_contacts, save_contacts

def is_valid_contact(name, phone):
    if not name.replace(" ", "").isalpha():
        print("❌ Error: Name must be a string.")
        return False
    if not phone.isdigit():
        print("❌ Error: Phone number must be numeric.")
        return False
    return True

def add_contact():
    contacts = load_contacts()
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    if not is_valid_contact(name, phone):
        return

    for c in contacts:
        if c['Phone'] == phone:
            print("❌ Error: Phone number already exists for another contact.")
            return

    new_contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
    contacts.append(new_contact)
    save_contacts(contacts)
    print("✅ Contact added successfully!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("⚠️ No contacts found.")
        return
    print("===== All Contacts =====")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. Name   : {c['Name']}")
        print(f"   Phone  : {c['Phone']}")
        print(f"   Email  : {c['Email']}")
        print(f"   Address: {c['Address']}\n")

def search_contact():
    term = input("Enter search term (name/email/phone): ").strip().lower()
    contacts = load_contacts()
    found = False
    for c in contacts:
        if term in c['Name'].lower() or term in c['Phone'] or term in c['Email'].lower():
            print("\n🔍 Search Result:")
            print(f"Name   : {c['Name']}")
            print(f"Phone  : {c['Phone']}")
            print(f"Email  : {c['Email']}")
            print(f"Address: {c['Address']}")
            found = True
            break
    if not found:
        print("❌ No matching contact found.")

def remove_contact():
    phone = input("Enter the phone number of the contact to delete: ").strip()
    contacts = load_contacts()
    for i, c in enumerate(contacts):
        if c['Phone'] == phone:
            confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ").lower()
            if confirm == 'y':
                del contacts[i]
                save_contacts(contacts)
                print("🗑️ Contact deleted successfully!")
            else:
                print("❌ Deletion cancelled.")
            return
    print("❌ Contact not found.")
