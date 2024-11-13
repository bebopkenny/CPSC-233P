# contacts.py
# Name: [Your Name]
# Date: [Current Date]
# Purpose: To manage a contact list for Tuffy Titan

def add_contact(contacts, id, first_name, last_name):
    """Add a contact to the contact dictionary."""
    if id in contacts:
        return "error"
    contacts[id] = [first_name, last_name]
    return {id: [first_name, last_name]}

def modify_contact(contacts, id, first_name, last_name):
    """Modify an existing contact in the contact dictionary."""
    if id not in contacts:
        return "error"
    contacts[id] = [first_name, last_name]
    return {id: [first_name, last_name]}

def delete_contact(contacts, id):
    """Delete a contact from the contact dictionary."""
    if id not in contacts:
        return "error"
    deleted_contact = {id: contacts.pop(id)}
    return deleted_contact

def sort_contacts(contacts):
    """Sort the contacts dictionary by last name and then first name."""
    sorted_contacts = dict(sorted(contacts.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
    return sorted_contacts

def find_contact(contacts, find):
    """Find contacts that match the search criteria."""
    found_contacts = {}
    if find.isdigit() and find in contacts:
        found_contacts[find] = contacts[find]
    
    for id, (first, last) in contacts.items():
        if find.lower() in first.lower() or find.lower() in last.lower():
            found_contacts[id] = [first, last]

    return sort_contacts(found_contacts)

