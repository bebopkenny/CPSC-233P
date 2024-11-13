# weather.py
# Name: Kenny Garcia
# Date: 10/16/2024
# Purpose: Making the weather function using calendar 

import json
import calendar

def read_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def max_temperature(data, date):
    temps = [readings['t'] for dt, readings in data.items() if date in dt]
    return max(temps) if temps else None

def min_temperature(data, date):
    temps = [readings['t'] for dt, readings in data.items() if date in dt]
    return min(temps) if temps else None

def max_humidity(data, date):
    humidities = [readings['h'] for dt, readings in data.items() if date in dt]
    return max(humidities) if humidities else None

def min_humidity(data, date):
    humidities = [readings['h'] for dt, readings in data.items() if date in dt]
    return min(humidities) if humidities else None

def tot_rain(data, date):
    rains = [readings['r'] for dt, readings in data.items() if date in dt]
    return sum(rains) if rains else 0.0

def report_daily(data, date):
    report = "========================= DAILY REPORT ========================\n"
    report += "Date                      Time  Temperature  Humidity  Rainfall\n"
    report += "====================  ========  ===========  ========  ========\n"
    
    for dt, readings in data.items():
        if date in dt:
            time = dt[8:10] + ':' + dt[10:12] + ':' + dt[12:14]
            formatted_date = f"{calendar.month_name[int(dt[4:6])]} {int(dt[6:8])}, {dt[:4]}"
            report += f"{formatted_date}      {time}           {readings['t']}        {readings['h']}      {readings['r']:.2f}\n"
    
    return report

def report_historical(data):
    report = "============================== HISTORICAL REPORT ===========================\n"
    report += "              Minimum      Maximum   Minumum   Maximum     Total\n"
    report += "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    report += "====================  ===========  ===========  ========  ========  ========\n"

    dates = set(dt[:8] for dt in data.keys())
    for date in sorted(dates):
        min_temp = min_temperature(data, date)
        max_temp = max_temperature(data, date)
        min_hum = min_humidity(data, date)
        max_hum = max_humidity(data, date)
        total_rain = tot_rain(data, date)
        formatted_date = f"{calendar.month_name[int(date[4:6])]} {int(date[6:8])}, {date[:4]}"
        report += f"{formatted_date}               {min_temp}           {max_temp}        {min_hum}        {max_hum}      {total_rain:.2f}\n"
    
    return report