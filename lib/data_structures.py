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

def get_names(spicy_foods):
    return [key["name"] for key in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return[key for key in spicy_foods if key["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for key in spicy_foods:
        heat_level = "🌶" * key["heat_level"]
        print(f'{key["name"]} ({key["cuisine"]}) | Heat Level: {heat_level}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if(food["cuisine"] == cuisine):
            return food
        

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if(food["heat_level"] > 5):
            heat_emojis = "🌶" * food["heat_level"]
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_emojis}')

def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        total = total + food["heat_level"]
        print(total / 3)
    return total / 3

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
        
