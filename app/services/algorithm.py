import random
from data.bergen.full_random_bergen import full_random_bergen as random_bergen
# need to import rest of data

# activity limits
film_activities = [
    "Movie",
    "Cinema",
    "Theatre",
    "Stand up"
]
food_activities = [
    "Restaurant",
    "Homemade dinner",
    "Cooking class"
]
# Activity objects
cities_categories = {
    "stavanger": {
        "first date": None, 
        "active": None,
        "creative": None,
        "adventurous": None,
        "random": random_stavanger
    },
    "bergen": {
        "first date": first_date_bergen, 
        "active": active_bergen,
        "creative": creative_bergen,
        "adventurous": adventurous_bergen,
        "random": random_bergen
    },
    "oslo": {
        "first date": None, 
        "active": None,
        "creative": None,
        "adventurous": None,
        "random": random_oslo
    },
    "trondheim": {
        "first date": None, 
        "active": None,
        "creative": None,
        "adventurous": None,
        "random": random_trondheim
    },
}


# Recursive algorithm to get random activities
def get_random_activities(activities_city, n, activities_list=None, is_film=False, is_food=False, is_hike=False, attempts=0):
    if activities_list is None:
        activities_list = []
    if attempts > 20:
        return activities_list

    # selects the random activities
    activity_keys = list(activities_city.keys())
    random_activity = random.choice(activity_keys)
    value = activities_city[random_activity]

    # checks the limit for specific activities and rerolls if limit is reached
    if (is_film and random_activity in film_activities) or \
       (is_food and random_activity in food_activities) or \
       (is_hike and random_activity == "Run/hike"):
        return get_random_activities(activities_city, n, activities_list, is_film, is_food, is_hike, attempts + 1)

    # function body
    if isinstance(value, list):
        if random_activity not in activities_list:
            print(f"----------\nActivity selected: {random_activity}!")
            activities_list.append(random_activity)
            n -= 1
            is_film, is_food, is_hike = set_limit(random_activity, is_film, is_food, is_hike)
            get_activity_info(value)
    elif isinstance(value, dict) and len(value) > 1:
        selection_keys = list(value.keys())
        selection = random.choice(selection_keys)
        selection_value = activities_city[random_activity][selection]
        if isinstance(selection_value, list) and selection not in activities_list:
            print(f"----------\nActivity selected: {selection}!")
            activities_list.append(random_activity)
            n -= 1
            is_film, is_food, is_hike = set_limit(random_activity, is_film, is_food, is_hike)
            get_activity_info(selection_value)
        elif isinstance(selection_value, dict) and len(selection_value) >= 1:
            nested_activity = get_random_activities(selection_value, 1, [], is_film, is_food, is_hike)
            if nested_activity and nested_activity[0] not in activities_list:
                print(f"----------\nActivity selected: {nested_activity[0]}!")
                activities_list.append(random_activity)
                n -= 1
                is_film, is_food, is_hike = set_limit(random_activity, is_film, is_food, is_hike)
    elif isinstance(value, dict) and len(value) == 1:
        nested_activity = get_random_activities(value, 1, [], is_film, is_food, is_hike)
        if nested_activity and nested_activity[0] not in activities_list:
            print(f"----------\nActivity selected: {nested_activity[0]}!")
            activities_list.append(random_activity)
            n -= 1
            is_film, is_food, is_hike = set_limit(random_activity, is_film, is_food, is_hike)
    # base case
    if n > 0:
        return get_random_activities(activities_city, n, activities_list, is_film, is_food, is_hike, attempts + 1)
    return f"----------\nYour date for the evening: {activities_list}"
    

# Used in the algorithm to get activity information
def get_activity_info(info_dict):
    for key, value in info_dict.items():
        print(f"{key}: {value}")

# Sets a boolean to True, to prevent similar reoccuring activities
def set_limit(random_activity, is_film, is_food, is_hike):
    if random_activity in film_activities:
        is_film = True
    elif random_activity in food_activities:
        is_food = True
    elif random_activity == "Run/hike":
        is_hike = True
    return is_film, is_food, is_hike

# Get a city from the frontend by user input
def get_city(user_city):
    city = user_city.lower()
    return city

# Get an activity category from the frontend by user input
def get_activities_by_category(user_category, city):
    category = user_category.lower()
    return cities_categories[city][category]

# Get number of activities from the frontend by user input
def get_number_activities(user_number):
    if 0 < user_number < 5:
        return user_number
    else: 
        raise ValueError("Amount must be between 1 and 4")
