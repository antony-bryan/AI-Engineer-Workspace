import pandas as pd

student_scores_dict = {
    "student":["Antony", "Bryan", "Nami"],
    "score":[90, 92, 95],
}

student_score_dataframe = pd.DataFrame(student_scores_dict)

print(student_score_dataframe)
print("\n")

# Loop through a dataframe

# for key,value in student_score_dataframe.items():
#     print(value)

#Loop through rows of a dataframe

for (index, row) in student_score_dataframe.iterrows():
    print(index)
    print(row)

for (index, row) in student_score_dataframe.iterrows():
    if row.student == "Bryan":
        print(row.score)
