# main.py

from contact_operations import add_contact, view_contacts, search_contact, remove_contact
from file_handler import load_contacts

def show_menu():
    print("\n=========== MENU ===========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")
    print("============================")

def main():
    print("📒 Welcome to the Contact Book CLI System!")
    print("Loading contacts from contacts.csv... Done!")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            remove_contact()
        elif choice == '5':
            print("👋 Thank you for using the Contact Book CLI System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
