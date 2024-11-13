# contacts.py
# Name: Kenny Garcia
# Date: 10/29/2024
# Purpose: Created a contacts class to make functions for inputting and deleting contact information

import json
from typing import Dict, List, Union

class Contacts:
    def __init__(self, filename: str = "contacts.json"):
        self.filename = filename
        self.data = {}
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}
    
    def add_contact(self, id: str, first_name: str, last_name: str) -> Union[str, Dict]:
        if id in self.data:
            return "Phone number already exists."
        self.data[id] = [first_name, last_name]
        self.data = dict(sorted(self.data.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
        self._write_to_file()
        return {id: self.data[id]}
    
    def modify_contact(self, id: str, first_name: str, last_name: str) -> Union[str, Dict]:
        if id not in self.data:
            return "Invalid phone number."
        self.data[id] = [first_name, last_name]
        self.data = dict(sorted(self.data.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
        self._write_to_file()
        return {id: self.data[id]}
    
    def delete_contact(self, id: str) -> Union[str, Dict]:
        if id not in self.data:
            return "Invalid phone number."
        deleted_contact = {id: self.data.pop(id)}
        self._write_to_file()
        return deleted_contact
    
    def get_contacts(self) -> List[Dict[str, Union[str, List[str]]]]:
        return [{"Phone": k, "First Name": v[0], "Last Name": v[1]} for k, v in self.data.items()]
    
    def set_filename(self, filename: str):
        self.filename = filename
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

    def _write_to_file(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)