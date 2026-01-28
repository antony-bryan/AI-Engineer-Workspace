#Extratc he names of the invited people from the file
names = []

with open("./Python/Day_24_Files_Directories_and_Paths\Mail_Merge_Project/Input/Names/invited_names.txt") as file:
    for line in file:
        names.append(line.strip())
        
# with open("./Python/Day_24_Files_Directories_and_Paths\Mail_Merge_Project/Input/Names/invited_names.txt") as file:
#     names = file.readlines()

        
# print(names)
# ['Aang\n', 'Zuko\n', 'Appa\n', 'Katara\n', 'Sokka\n', 'Momo\n', 'Uncle Iroh\n', 'Toph']

# Extract the mail template
mail_template = ""

with open("Python\Day_24_Files_Directories_and_Paths\Mail_Merge_Project\Input\Letters\starting_letter.txt") as file:
    mail_template = file.read()
    
#Creating Personalised mail and writing it in separate file for each person

mail = ""

for name in names:
    mail = mail_template
    mail = mail.replace("[name]",name)
    with open(f"Python\Day_24_Files_Directories_and_Paths\Mail_Merge_Project\Output\ReadyToSend\mail_for_{name}.txt", mode="w") as file:
        file.write(mail)
    

