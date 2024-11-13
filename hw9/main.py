# main.py
# Name: Kenny Garcia
# Date: 11/12/2024
# Purpose: Use the flight module to create passenger flight information

from flights import Flights
from datetime import datetime

def display_menu():
    print("\n      *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU\n")
    print("1. Add flight")
    print("2. Print flight schedule")
    print("3. Set flight schedule filename")
    print("9. Exit the program")

def add_flight(flights):
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")
    flight_number = input("Enter flight number: ")
    departure = input("Enter departure time (HHMM): ")
    arrival = input("Enter arrival time (HHMM): ")
    next_day = input("Is arrival next day (Y/N): ").upper()

    # Call the add_flight method from Flights class
    success = flights.add_flight(origin, destination, flight_number, departure, next_day, arrival)
    if not success:
        print("Invalid time format. Please try again.")
    else:
        print("Flight added successfully.")

def print_flight_schedule(flights):
    print("\n================== FLIGHT SCHEDULE ==================")
    print(f"{'Origin':<6} {'Destination':<11} {'Number':<6} {'Departure':<9} {'Arrival':<8} {'Duration'}")
    print(f"{'======':<6} {'===========':<11} {'======':<6} {'=========':<9} {'========':<8} {'========'}")
    
    flight_list = flights.get_flights()
    for flight in flight_list:
        print(f"{flight[0]:<6} {flight[1]:<11} {flight[2]:<6} {flight[3]:<9} {flight[4]:<8} {flight[5]}")

def main():
    flights = Flights("flights.json")
    
    while True:
        display_menu()
        choice = input("Enter menu choice: ")
        
        if choice == '1':
            add_flight(flights)
        elif choice == '2':
            print_flight_schedule(flights)
        elif choice == '3':
            filename = input("Enter new flight schedule filename: ")
            flights = Flights(filename)
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()