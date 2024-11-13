# people.py
# Name: Kenny Garcia
# Date: 11/05/2024
# Purpose: Creating a person class for faculty and student functions

class Person:
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name


class Faculty(Person):
    def __init__(self, first_name, last_name, department):
        super().__init__(first_name, last_name)
        self.department = department


class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.classyear = None
        self.major = None
        self.advisor = None

    def set_class(self, class_year):
        self.classyear = class_year

    def set_major(self, major):
        self.major = major

    def set_advisor(self, faculty):
        self.advisor = faculty
