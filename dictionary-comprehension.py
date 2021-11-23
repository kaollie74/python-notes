import random

# DICTIONARY COMPREHENSION

# new_dict = {new_key: new_value for item in list}

# EXAMPLE 1
# 1. iterate over "list1"
# 2. set the key as the el
# 3. set the value of each key with a random number
list1 = ["Kyle", "Terwey", "Elias", "Dylan", "Larson", "Price"]

new_dict_1 = {el: random.randint(1, 100) for el in list1}

# Note the numbers a random so these will change
# however the names for keys should be consistent.

# print(new_dict_1)  # OUTPUT: {'Kyle': 27, 'Terwey': 23, 'Elias': 40, 'Dylan': 21, 'Larson': 22, 'Price': 97}

"""End EXAMPLE 1 """

# EXAMPLE 2
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# string_list = sentence.split(" ")
# OUTPUT: ['What', 'is', 'the', 'Airspeed', 'Velocity', 'of', 'an', 'Unladen', 'Swallow?']
#
# result = {el: len(el) for el in string_list}
#
#
# print(result)
# OUTPUT: {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

"""End EXAMPLE 2 """

# Dictionary comprehension with condition

# 1. interate of "new_dict_1"
# 2. Condition: if value is over 50 set to new dictionary

pass_students = {student: score for (student, score) in new_dict_1.items() if score > 50}
print(pass_students)  # OUTPUT >> {'Kyle': 62, 'Elias': 66, 'Larson': 76, 'Price': 59}


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# calculate temp from Celcius to Fahrenheit
weather_f = {key: (value * 1.8) + 32 for (key, value) in weather_c.items()}

print(weather_f)
