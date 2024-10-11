# Just learning pandas, nothing fancy here

import pandas

def celcius_to_fahrenheit(temp):
    return (temp * 1.8) + 32

data = pandas.read_csv("day25_weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average_temp = data["temp"].mean()
print(average_temp)

max_temp = data["temp"].max()
print(max_temp)

monday_row = data[data.day == "Monday"]
print(monday_row)

hottest_day = data[data.temp == data.temp.max()]
print(hottest_day)

monday = data[data.day == "Monday"]
print(monday.condition)

monday_fahrenheit_temp = celcius_to_fahrenheit(monday.temp)
print(monday_fahrenheit_temp)

new_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65]
}
new_data = pandas.DataFrame(new_dict)
new_data.to_csv("day25_new_data.csv")
print(new_data)