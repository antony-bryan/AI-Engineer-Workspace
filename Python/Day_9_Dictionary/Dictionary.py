Programming_Dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

print(Programming_Dictionary["Bug"])

Programming_Dictionary["Loop"] = "The action of doing something over and over again."
print(Programming_Dictionary)

empty_dict = {}

# Wipe an existing dictionary
# Programming_Dictionary = {}
# print(Programming_Dictionary)

# Edit an item in dictionary

Programming_Dictionary["Bug"] = "A moth in your computer."
print(Programming_Dictionary)


for key in Programming_Dictionary:
    print(key)
    print(Programming_Dictionary[key])