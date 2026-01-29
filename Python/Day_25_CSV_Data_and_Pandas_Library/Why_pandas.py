# data = []

# with open("Python\Day_25_CSV_Data_and_Pandas_Library\weather_data.csv") as file:
#     data = [line.strip() for line in file]

#To work with CSV we have a module Called csv

# import csv

# with open("Python\Day_25_CSV_Data_and_Pandas_Library\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

#So much faff only to get the temp values out of the csv file. that is why we will use
#Pandas library

import pandas as pd

data = pd.read_csv("Python\Day_25_CSV_Data_and_Pandas_Library\weather_data.csv")

# print(data)

print(data["temp"])