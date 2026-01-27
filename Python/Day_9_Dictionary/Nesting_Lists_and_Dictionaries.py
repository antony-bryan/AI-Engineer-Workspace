capitals ={
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart","Berlin"],
}

#print Lille
print(travel_log["France"][1])


#Nested List
nested_list = ["A", "b", ["C", "D"]]

print(nested_list[2][1])

travel_log = {
    "France": {
        "number_of_visits": 8,
        "cities_visied": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "number_of_visits": 4,
        "cities_visied": ["Stuttgart","Berlin"]
    },
}

#print Stuttgart from travel_log
print(travel_log["Germany"]["cities_visied"][0])
