number = [1,2,3]
new_list = [n+1 for n in number]

print(new_list)

name = "Bryan"
new_list = [letter for letter in name]

print(new_list)

new_list = [n*2 for n in range(1,5)]

print(new_list)

names = ["Bryan", "Nami", "Hari", "Ameeru"]

short_names = [name for name in names if len(name) <= 4]
print(short_names)