
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# Define a function get_names() that takes a list of spicy_foods
# and returns a list of strings with the names of each spicy food.

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

# Define a function get_spiciest_foods() that takes a list of spicy_foods and returns a list of dictionaries where the heat level of the food is greater than 5.

def get_spiciest_foods(spicy_foods):
    names = []
    for spiciest_food in spicy_foods:
        if spiciest_food["heat_level"] > 5:
            names.append(spiciest_food)
    return names

# # print_spicy_foods()
# Define a function print_spicy_foods() that takes a list of spicy_foods and output to the terminal each spicy food in the following format using print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶.

# HINT: you can use times (*) with a stringLinks to an external site. to produce the correct number of "🌶" emojis.

def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'* food['heat_level']}")
    

# # get_spicy_food_by_cuisine()
# Define a function get_spicy_food_by_cuisine() that takes a list of spicy_foods and a string representing a cuisine, and returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food['cuisine'] == cuisine:
            return spicy_food

# Define a function print_spiciest_foods() that takes a list of spicy_foods and outputs to the terminal ONLY the spicy foods that have a heat level greater than 5, in the following format:

def print_spiciest_foods(spicy_foods):
    for spiciest_food in spicy_foods:
        if spiciest_food['heat_level'] > 5:
            print(f"{spiciest_food['name']} ({spiciest_food['cuisine']}) | Heat Level: {'🌶'* spiciest_food['heat_level']}")

# get_average_heat_level()
# Define a function average_heat_level() that takes a list of spicy_foods and returns an integer representing the average heat level of all the spicy foods in the array. Recall that to derive the average of a collection, you need to calculate the total and divide number of elements in the collection.

def get_average_heat_level(spicy_foods):
    total_heat = 0
    count = 0
    for spicy_food in spicy_foods:
        total_heat += spicy_food['heat_level']
        count +=1
    return total_heat // count

# create_spicy_food()
# Define a function create_spicy_food() that takes a list of spicy_foods and a new spicy_food and returns the original list with the new spicy_food added.

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
