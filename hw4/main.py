# main.py
# Name: [Your Name]
# Date: [Current Date]
# Purpose: To provide a user interface for managing Tuffy Titan contacts

from contacts import *

def display_menu():
    """Display the main menu."""
    print("\n      *** TUFFY TITAN CONTACT MAIN MENU")
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list")
    print("5. Find contact")
    print("6. Exit the program")

def print_contacts(contacts):
    """Print the formatted contact list."""
    sorted_contacts = sort_contacts(contacts)
    print("\n==================== CONTACT LIST ====================")
    print(f"{'Last Name':<20} {'First Name':<20} {'Phone':<10}")
    print("====================  ====================  ==========")
    for id, (first, last) in sorted_contacts.items():
        print(f"{last:<20} {first:<20} {id}")

def main():
    """Main driver program."""
    contacts = {}
    
    while True:
        display_menu()
        choice = input("Enter menu choice: ")

        if choice == "1":  # Add contact
            phone = input("Enter phone number: ")
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            result = add_contact(contacts, phone, first, last)
            if result == "error":
                print("Phone number already exists.")
            else:
                print(f"Added: {first} {last}.")

        elif choice == "2":  # Modify contact
            phone = input("Enter phone number: ")
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            result = modify_contact(contacts, phone, first, last)
            if result == "error":
                print("Phone number does not exist.")
            else:
                print(f"Modified: {first} {last}.")

        elif choice == "3":  # Delete contact
            phone = input("Enter phone number: ")
            result = delete_contact(contacts, phone)
            if result == "error":
                print("Phone number does not exist.")
            else:
                first, last = result[phone]
                print(f"Deleted: {first} {last}.")

        elif choice == "4":  # Print contact list
            print_contacts(contacts)

        elif choice == "5":  # Find contact
            search = input("Enter search string: ")
            found_contacts = find_contact(contacts, search)
            if found_contacts:
                print("\n================== FOUND CONTACT(S) ==================")
                print(f"{'Last Name':<20} {'First Name':<20} {'Phone':<10}")
                print("====================  ====================  ==========")
                for id, (first, last) in found_contacts.items():
                    print(f"{last:<20} {first:<20} {id}")
            else:
                print("No contacts found.")

        elif choice == "6":  # Exit
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

