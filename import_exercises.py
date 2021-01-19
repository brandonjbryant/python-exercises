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
 

with open('profiles.json') as f:
    data = json.load(f)
# ### import json
# profiles = json.load (open(profiles.json))

data[8]

# 1. Total number of users
#19 Users
len(data)
#len(profiles)

# 2. Number of active users
#9 Active
active_users = []
for user in range(len(data)):    
    if data[user]['isActive'] == True:
        active_users.append(data[user]['name'])
        
print(active_users)
len(active_users)

#if profiles[0]['isActive']
#   print[(1)
#else 
#    print(0)
###Another route:
# len([profile for profile in profiles if profile['isActive'])


# 3. Number of inactive users
#10 inactive
inactive_users = []
for user in range(len(data)):    
    if data[user]['isActive'] == False:
        inactive_users.append(data[user]['name'])
        
print(inactive_users)
len(inactive_users)

#len([profile for profile in profiles if not profile['isActive'])

# 4. Grand total of balances for all users
#52667.02
grand_total = []
for user in range(len(data)):    
    grand_total.append(data[user]['balance'])
    

def string_to_float(x):
    return float(x.replace(',','').replace('$',''))

grand_total = [string_to_float(balance) for balance in grand_total]

sum(grand_total)

#def clean_balance(balance):
#   balance = balance.replace(',' ,'')
#   balance = balance.replace('$' ,'')
#   return float (balance)

###extracting the balance values

####remove the 


#balance = profiles

# 5. Average balance per user
#2771.95
average_balance = round(sum(grand_total)/len(data),2)
average_balance

#sum(balances)/len(balances)

# 6. User with the lowest balance
#$1,214.10 Avery Flynn
print(min(grand_total))

[user['balance'] +' '+ user['name'] for user in data if user['balance'] == '$1,214.10']

#user-WITH_LOWEST_BA

# 7. User with the highest balance
#$3,919.64 Fay Hammond

print(max(grand_total))

[user['balance'] +' '+ user['name'] for user in data if user['balance'] == '$3,919.64']


# 8. Most common favorite fruit
#Most common favorite fruit
#Strawberry
fav_fruit = [user['favoriteFruit'] for user in data]
fav_fruit

import statistics
statistics.mode(fav_fruit)



# 9. Least most common favorite fruit
#Least most common favorite fruit
#Apples with 4
print(sorted(fav_fruit))
print()

print('There are', fav_fruit.count('apple'), 'users with favorite Apples')
print('There are', fav_fruit.count('banana'), 'users with favorite Banana')
print('There are', fav_fruit.count('strawberry'), 'users with favorite Strawberry')


# 10. Total number of unread messages for all users
greeting = [user['greeting'] for user in data]


def extract_num(string):
    for char in string:
        if char.isdigit():
            return int(char)
        
message_quantity_list = [extract_num(message) for message in greeting]
print(f'Total number of unread messages: {sum(message_quantity_list)}')
