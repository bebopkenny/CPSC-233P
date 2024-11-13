# main.py
# Name: Kenny Garcia
# Date: 10/29/2024
# Purpose: Use the class from contacts.py to make a contact list

import sys
from contacts import Contacts

def display_menu():
    print("      *** TUFFY TITAN CONTACT MAIN MENU")
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list")
    print("5. Set contact filename")
    print("6. Exit the program")

def main():
    contacts = Contacts()
    while True:
        display_menu()
        choice = input("Enter menu choice: ")
        
        if choice == '1':
            phone = input("Enter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = contacts.add_contact(phone, first_name, last_name)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Added: {first_name} {last_name}.")

        elif choice == '2':
            phone = input("Enter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = contacts.modify_contact(phone, first_name, last_name)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Modified: {first_name} {last_name}.")

        elif choice == '3':
            phone = input("Enter phone number: ")
            result = contacts.delete_contact(phone)
            if isinstance(result, str):
                print(result)
            else:
                deleted = result[phone]
                print(f"Deleted: {deleted[0]} {deleted[1]}.")

        elif choice == '4':
            contact_list = contacts.get_contacts()
            print("\n==================== CONTACT LIST ====================")
            print("Last Name             First Name            Phone")
            print("====================  ====================  ==========")
            for contact in contact_list:
                print(f"{contact['Last Name']:20}  {contact['First Name']:20}  {contact['Phone']}")

        elif choice == '5':
            filename = input("Enter new contact filename: ")
            contacts.set_filename(filename)
            print(f"Contact filename set to {filename}.")

        elif choice == '6':
            print("Exiting program.")
            sys.exit(0)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
