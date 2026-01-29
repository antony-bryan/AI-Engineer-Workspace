import pandas as pd

data = pd.read_csv("Python\Day_25_CSV_Data_and_Pandas_Library\weather_data.csv")

# print(type(data["temp"]))

# print(type(data))

# temp_list = data["temp"].to_list()

# print(temp_list)

# print(f"Average temperature = {data["temp"].mean()}")

# print(f"max temp = {data['temp'].max()}")

# print(data.columns) #to list all the columns in the dataframe

# #Get dat in the column
# print(data['condition'])
# #or
# print(data.condition)

## ----------------------------------

## printing a row

# print(data[data.day == "Monday"])

##printing the row which had the maximum temp of the week

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday['temp'])

# temp_f = (monday.temp[0] * (9/5)) + 32

# print(temp_f)

## ----------------------------------

#Creating Data from scratch

data_dict = {
    "students": ["James","Arjun","Gojo"],
    "marks": [60,70,90]
}
data_frame = pd.DataFrame(data_dict)
print(data_frame)

data_frame.to_csv("Python/Day_25_CSV_Data_and_Pandas_Library/new_csv.csv")

