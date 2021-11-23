import random

# DICTIONARY COMPREHENSION

# new_dict = {new_key: new_value for item in list}

# EXAMPLE
# 1. iterate over "list1"
# 2. set the key as the el
# 3. set the value of each key with a random number
list1 = ["Kyle", "Terwey", "Elias", "Dylan", "Larson", "Price"]

new_dict_1 = {el: random.randint(1, 100) for el in list1}

# Note the numbers a random so these will change
# however the names for keys should be consistent.

# print(new_dict_1)  # OUTPUT: {'Kyle': 27, 'Terwey': 23, 'Elias': 40, 'Dylan': 21, 'Larson': 22, 'Price': 97}

#######################################################################################################################

# Dictionary comprehension with condition

# 1. interate of "new_dict_1"
# 2. Condition: if value is over 50 set to new dictionary

pass_students = {student: value for (student, value) in new_dict_1.items() if value > 50}
print(pass_students)  # OUTPUT >> {'Kyle': 62, 'Elias': 66, 'Larson': 76, 'Price': 59}
