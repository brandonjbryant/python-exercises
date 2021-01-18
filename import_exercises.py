# ### Import and test 3 of the functions from your functions exercise file.
# * Import each function in a different way:
#     1. import the module and refer to the function with the . syntax
#     2. use from to import the function directly
#     3. use from and give the function a different name
import function_exercises 

from function_exercises import is_consonant as find_con
from function_exercises import normalize_name

assert function_exercises.is_two("2")
assert normalize_name("First Name") == "first_name"
assert find_con("z")


# ### How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?(9 Combinations)
from itertools import product

number_of_combinations = len(list(product("abc", "123")))
print(f"{number_of_combinations} combinations")

# ### How many different ways can you combine two of the letters from "abcd"?


from itertools import combinations 

number_of_combinations = len(list(combinations("abcd", 2)))
print(f"{number_of_combinations} combinations")

# ### Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
import json

profiles = open("profiles.json")
list_of_profiles = json.load(profiles)
list_of_profiles

list_of_profiles[0]
len(list_of_profiles)

# 1. Total number of users
total_users = len(list_of_profiles)
total_users