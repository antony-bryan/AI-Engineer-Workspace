import pandas as pd

INPUT_CSV = "Python/Day_25_CSV_Data_and_Pandas_Library/Squirrel_Data.csv"
OUTPUT_CSV = "Python/Day_25_CSV_Data_and_Pandas_Library/Unique_color_Count.csv"

data = pd.read_csv(INPUT_CSV)

# print(data.info())

# result = (
#     data["Primary Fur Color"]
#     .value_counts()
#     .reindex()
# )

# result.columns = ["Fur Color", "Count"]

# print(result)

# result.to_csv(OUTPUT_CSV)



unique_colors = data["Primary Fur Color"].unique()

color_count = []

for color in unique_colors:
    if pd.notna(color):
        color_dataframe = data[data["Primary Fur Color"] == color]
        color_count.append(color_dataframe.__len__())

print(color_count)



data_dict = {
    "Fur Color" : ['Gray', 'Cinnamon', 'Black'],
    "Count" : color_count,
}

data_frame = pd.DataFrame(data_dict)

data_frame.to_csv(OUTPUT_CSV)