import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "my_file.txt")

new_file_path = os.path.join(script_dir, "new_file.txt")
# file = open(file_path)

# contents = file.read()
# print(contents)
# file.close()

with open("./my_file.txt") as file:
    contents = file.read()
    print(contents + " Releative file path")
    

with open(file_path) as file:
    contents = file.read()
    print(contents)

#If the file does no exist then it will be automatically created
with open(new_file_path, mode="w") as file:
    file.write("New text.")

with open(file_path, mode="w") as file:
    file.write("New text.")
    
with open(file_path, mode="a") as file:
    file.write("\nAdditional Text.")    