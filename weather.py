import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# DONE Takes a temperature and returns it in string format with the degrees & celcius symbols. 

def format_temperature(temp):  
    return f"{temp}{DEGREE_SYBMOL}"
# Args: temp: A string representing a temperature. Returns:  A string contain the temperature and "degrees celcius."


# DONE  Converts and ISO formatted date into a human readable format.

def convert_date(iso_string):  
    date = datetime.fromisoformat(iso_string)
    final_date = date.strftime("%A %d %B %Y")
    return final_date
# Args: iso_string: An ISO date string. Returns: A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
     

# DONE Converts an temperature from farenheit to celcius.

def convert_f_to_c(temp_in_farenheit): 
     temp_in_celsius = (float(temp_in_farenheit) - 32) * (5/9)
     return float(f"{temp_in_celsius:.1f}")
 #Args:    temp_in_farenheit: float representing a temperature.
 #Returns: A float representing a temperature in degrees celcius, rounded to 1dp.



# DONE Calculates the mean value from a list of numbers.

def calculate_mean(weather_data):
    list = [float(value) for value in weather_data]
    total = sum(list)
    average = len(list)
    answer = total / average
    return float(answer)
# Args: weather_data: a list of numbers.
# Returns: A float representing the mean value.



# DONE  Reads a csv file and stores the data in a list. 

def load_data_from_csv(csv_file): 
    my_list = []
    with open(csv_file, mode ="r") as my_file:
        csv_reader = csv.reader(my_file)
        next(csv_reader)
        for row in csv_reader:
            if row:
                fixed = int(row[-2])
                fixed2 = int(row[-1])
                anything = [row[0], fixed, fixed2]
                my_list.append(anything)
    return my_list
# Args: csv_file: a string representing the file path to a csv file.
# Returns: list of lists, where each sublist is a (non-empty) line in the csv file.



# DONE Calculates the minimum value in a list of numbers.   DONE 

def find_min(weather_data):
    if not weather_data:
       return ()    
    min_val = min(weather_data)
    position = weather_data.index(min_val)
    index = 0 
    for temperature in weather_data:
        if temperature == min_val:
            position = index
        index += 1
    answer = (float(min_val), position)
    return (answer)
#Arg :weather_data: list of numbers. Return: The minium value and it's position in the list.



# DONE Calculates the maximum value in a list of numbers.
def find_max(weather_data):
    if not weather_data:
       return ()    
    max_val = max(weather_data)
    position = weather_data.index(max_val)
    index = 0 
    for temperature in weather_data:
        if temperature == max_val:
            position = index
        index += 1
    answer = (float(max_val), position)
    return (answer)
# Args: weather_data: A list of numbers.Returns:The maximum value and it's position in the list.


# DONE Outputs a summary for the given weather data.
def generate_summary(weather_data):
    dates = [data[0] for data in weather_data] 
    minimum_temperatures =[data[1] for data in weather_data]
    min_temp, min_index = find_min(minimum_temperatures)
    maximum_temperatures = [data[2] for data in weather_data]
    max_temp, max_index = find_max(maximum_temperatures)
    min_date = dates[min_index]
    max_date = dates[max_index]
    average_min = sum(minimum_temperatures) / len(minimum_temperatures)
    average_max = sum(maximum_temperatures) / len(maximum_temperatures)
    return (f"{len(dates)} Day Overview\n"
            f"  The lowest temperature will be {format_temperature(convert_f_to_c(min_temp))}, and will occur on {convert_date(min_date)}.\n"
            f"  The highest temperature will be {format_temperature(convert_f_to_c(max_temp))}, and will occur on {convert_date(max_date)}.\n"
            f"  The average low this week is {format_temperature(convert_f_to_c(average_min))}.\n"
            f"  The average high this week is {format_temperature(convert_f_to_c(average_max))}.\n")
# Args: weather_data: A list of lists, each sublist represents a day of weather data.
# Returns: string containing the summary information.



# Outputs a daily summary for the given weather data.
def generate_daily_summary(weather_data):
    x = []
    dates = [data[0] for data in weather_data] 
    min_temp =[data[1] for data in weather_data]
    max_temp = [data[2] for data in weather_data]
    for index in range(len(dates)):
        x.append(f"---- {convert_date(dates[index])} ----\n"
           f"  Minimum Temperature: {format_temperature(convert_f_to_c(min_temp[index]))}\n"
           f"  Maximum Temperature: {format_temperature(convert_f_to_c(max_temp[index]))}\n\n")
    return ''.join(x) 


# Args: weather_data: list of lists, where each sublist represents a day of weather data.
# Returns: A string containing the summary information.

