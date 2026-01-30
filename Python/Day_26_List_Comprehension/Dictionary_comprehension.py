import random
names = ["Alex", "Beth", "Catherine", "Dave", "Trevor", "Franklin"]

student_score = {student:random.randint(1,100) for student in names}

print(student_score)

#passed_students = {student:student_score[student] for student in student_score if student_score[student] >= 60}
passed_students = {student:score for (student, score)in student_score.items() if score >= 60}

print(passed_students)