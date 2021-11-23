# new_list = [new_item for item in list]

# EXAMPLE
simple_list = [1, 2, 3]

new_list = [el for el in simple_list]
print(new_list)  # Output: [1, 2, 3]

# COMPREHENSION LIST WITH CONDITION
# new_list = [el for el in list if test]

# EXAMPLE
first_list = [1, 3, 5, 7, 9, 11]
new_list2 = [el for el in first_list if el > 7]
print(new_list2)  # OUTPUT : [9, 11]
