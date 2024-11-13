# flight.py
# Name: Kenny Garcia
# Date: 11/12/2024
# Purpose: Create a Flight class to record passenger's flights and save it on json file

import json
from datetime import datetime, timedelta

class Flights:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty schedule.")
    
    def add_flight(self, origin, destination, flight_number, departure, next_day, arrival):
        # Validate time format
        try:
            dep_time = datetime.strptime(departure, "%H%M")
            arr_time = datetime.strptime(arrival, "%H%M")
        except ValueError:
            return False

        # Adjust arrival time for next day
        if next_day == 'Y':
            arr_time += timedelta(days=1)

        # Calculate duration
        duration = arr_time - dep_time
        hours, minutes = divmod(duration.total_seconds() // 60, 60)
        duration_str = f"{int(hours)}:{int(minutes):02d}"

        # Append flight data
        flight = {
            'origin': origin,
            'destination': destination,
            'flight_number': flight_number,
            'departure': departure,
            'arrival': arrival,
            'next_day': next_day,
            'duration': duration_str
        }
        self.data.append(flight)

        # Write updated data back to file
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
        
        return True

    def get_flights(self):
        formatted_flights = []
        for flight in self.data:
            dep_time = datetime.strptime(flight['departure'], "%H%M")
            arr_time = datetime.strptime(flight['arrival'], "%H%M")
            if flight['next_day'] == 'Y':
                arr_time += timedelta(days=1)
            
            # Calculate duration
            duration = arr_time - dep_time
            hours, minutes = divmod(duration.total_seconds() // 60, 60)

            # Format departure and arrival strings
            dep_str = dep_time.strftime('%I:%M%p').lstrip('0').lower()
            if flight['next_day'] == 'Y':
                arr_str = '+' + arr_time.strftime('%I:%M%p').lstrip('0').lower()
            else:
                arr_str = arr_time.strftime('%I:%M%p').lstrip('0').lower()

            duration_str = f"{int(hours)}:{int(minutes):02d}"

            formatted_flights.append([
                flight['origin'],
                flight['destination'],
                flight['flight_number'],
                dep_str,
                arr_str,
                duration_str
            ])
        
        return formatted_flights