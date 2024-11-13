import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test01_AddContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 *** GIVEN: c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: add_contact(c, id = 7145551212, first_name = 'Richard', last_name = 'Stallman') *** EXPECT: c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates'], 7145551212: ['Richard', 'Stallman']} ***
        """
        c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        add_contact(c, id = 7145551212, first_name = 'Richard', last_name = 'Stallman')
        self.assertEqual(c, {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates'], 7145551212: ['Richard', 'Stallman']})
        print()

class Test02_AddContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 *** GIVEN: c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: r = add_contact(c, id = 7145551111, first_name = 'Richard', last_name = 'Stallman') *** EXPECT: r = 'error' ***
        """
        c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        r = add_contact(c, id = 7145551111, first_name = 'Richard', last_name = 'Stallman')
        self.assertEqual(r, 'error')
        print()

class Test03_ModifyContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 *** GIVEN: c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: modify_contact(c, id = 7145551111, first_name = 'Richard', last_name = 'Stallman') *** EXPECT: c = {7145551111: ['Richard', 'Stallman'], 5625553333: ['Bill', 'Gates']} ***
        """
        c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        modify_contact(c, id = 7145551111, first_name = 'Richard', last_name = 'Stallman')
        self.assertEqual(c, {7145551111: ['Richard', 'Stallman'], 5625553333: ['Bill', 'Gates']})
        print()

class Test04_ModifyContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 *** GIVEN: c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: r = modify_contact(c, id = 7145559999, first_name = 'Richard', last_name = 'Stallman') *** EXPECT: r = 'error' ***
        """
        c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        r = modify_contact(c, id = 7145559999, first_name = 'Richard', last_name = 'Stallman')
        self.assertEqual(r, 'error')
        print()

class Test05_DeleteContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 *** GIVEN: c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: delete_contact(c, id = 7145551111) *** EXPECT: c = {5625553333: ['Bill', 'Gates']} ***
        """
        c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        delete_contact(c, id = 7145551111)
        self.assertEqual(c, {5625553333: ['Bill', 'Gates']})
        print()

class Test06_DeleteContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test06 *** GIVEN: c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: r = delete_contact(c, id = 7145559999) *** EXPECT: r = 'error' ***
        """
        c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        r = delete_contact(c, id = 7145559999)
        self.assertEqual(r, 'error')
        print()

class Test07_SortContacts(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test07 *** GIVEN: c = {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: r = sort_contacts(c) *** EXPECT: r = {5625553333: ['Bill', 'Gates'], 7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs']} ***
        """
        c = {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        r = sort_contacts(c)
        self.assertEqual(r, {5625553333: ['Bill', 'Gates'], 7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs']})
        print()

class Test08_FindContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test08 *** GIVEN: c = {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: r = find_contact(c, find = 'jobs') *** EXPECT: r = {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs']} ***
        """
        c = {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        r = find_contact(c, find = 'jobs')
        self.assertEqual(r, {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs']})
        print()

class Test09_FindContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test09 *** GIVEN: c = {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: r = find_contact(c, find = '5625553333') *** EXPECT: r = {5625553333: ['Bill', 'Gates']} ***
        """
        c = {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        r = find_contact(c, find = '5625553333')
        self.assertEqual(r, {5625553333: ['Bill', 'Gates']})
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
