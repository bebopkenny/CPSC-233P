# main.py
# Name: Kenny Garcia
# Date: 10/16/2024
# Purpose: Use the functions in the weather module

import weather

def main():
    filename = 'default.json'
    weather_data = {}

    while True:
        print("\n      *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n")
        print("1. Set data filename")
        print("2. Add weather data")
        print("3. Print daily report")
        print("4. Print historical report")
        print("9. Exit the program")
        
        choice = input("\nEnter menu choice: ")

        if choice == '1':
            filename = input("Enter data filename: ")
            weather_data = weather.read_data(filename)
        elif choice == '2':
            date = input("Enter date (YYYYMMDD): ")
            time = input("Enter time (hhmmss): ")
            temp = int(input("Enter temperature: "))
            hum = int(input("Enter humidity: "))
            rain = float(input("Enter rainfall: "))
            datetime_key = date + time
            weather_data[datetime_key] = {'t': temp, 'h': hum, 'r': rain}
            weather.write_data(weather_data, filename)
        elif choice == '3':
            date = input("Enter date (YYYYMMDD): ")
            print(weather.report_daily(weather_data, date))
        elif choice == '4':
            print(weather.report_historical(weather_data))
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()