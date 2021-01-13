#prompt the user for a day of the week
today = input("What day of the week is it today? ")
if today == "Monday" :
        print("Today is Monday my friend! ")
else :
        print("Today is not Monday my friend! ")
    
    

#prompt the user for a day of the week, print out whether the day is a weekday or a weekend
today = input("What day of the week is it today? ")
today = today.lower()

if today == "saturday" or today == "sunday" :
    print(f"{today.capitalize()} is a weekend kinda day!!")
else:
    print(f"{today.capitalize()} is just a weekday, sorry pal.")

#create variables and make up values for
            #the number of hours worked in one week 
            
            #the hourly rate
   
            #how much the week's paycheck will be
            
            #write the python code that calculates the weekly paycheck. You get
            #paid time and a half if you work more than 40 hours
hours_worked = 80
hourly_pay = 100
 
if hours_worked <= 40:
    paycheck_amount = hours_worked * hourly_pay
else:
    # full 40 hours + overtime
    extra_grind_hours = hours_worked - 40
    light_work = 40 * hourly_pay
    extra_grind_pay_amount = extra_grind_hours * (hourly_pay* 1.5)
    paycheck_amount = light_work + extra_grind_pay_amount

print("My paycheck amount is " +str(paycheck_amount) + " dollars this week. Not bad for 80 hours!")



#Create an integer variable i with a value of 5.
    
#Create a while loop that runs so long as i is less than or equal to 15
i = 5
while i <= 15:
    print(i) 
    i += 1
#Each loop iteration, output the current value of i, then increment i by one.

#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
#Alter your loop to count backwards by 5's from 100 to -10.
#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 0
while i <= 100:
    print(i)
    i += 2

# Print output that counts backwards by 5 from 100 to -10.
i = 100
end = -10
while i >= end:
    print(i)
    i -= 5


#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
#7 times i
number = int(input("Choose a number "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


#Create this output:
#1
#22
#333
#4444
#55555
#666666
#7777777
#88888888
#999999999
for i in range(1, 10):
    print(i * str(i))


#Prompt the user for an odd number between 1 and 50.

#Use a loop and a break statement to continue prompting the user if they enter invalid input.

while True:
    user_choice= input("Choose an odd number between 1 and 50")
    
    if user_choice.isdigit():
        user_choice = int(user_choice)
    
        choice_maximum_met = user_choice > 1
        choice_minimum_met = user_choice < 50
        choice_is_odd = user_choice % 2 != 0
        
        if choice_maximum_met and choice_minimum_met and choice_is_odd:
            break
        else:
            print("Your choice must be an odd number greater than 1 and less than 50")
    else:
        print("Your choice must be a number ")
        
user_choice
#(Hint: use the isdigit method on strings to determine this). 
#Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
print(f"Skip {user_choice}")
print() # prints an extra new line

for i in range(1, 50, 2):
    if i == user_choice:
        print(f"try again: {i}")
        continue
    print(f"Odd Number: {i}")

user_choice = input("Choose a number ")
while (user_choice.isdigit() == False  
            or int(user_choice) <= 0):   
    print(f"{user_choice} Choose a positive number")
    user_choice = input("Choose a positive number")

user_choice = int(user_choice)

for i in range(user_choice + 1):
    print(i)


while user_choice >= 1:
    print(user_choice)
    user_choice -= 1


#FizzBuzz test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0: # explicit is better than implicit
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) 


# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# Example Output

# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125


while True:
    
    user_choice = int(input("Choose a number"))

    print("Here is your table!")

    print("number | squared | cubed")
    print("------ | ------- | -----")
    for i in range(1, user_choice + 1):
        print(f"{i}     |   {i**2}   |   {i ** 3}")
    
    continue_or_not = input("Press Y or yes to continue... \n")

    # if yoou don't want to continue, we're done here...
    if continue_or_not not in ["y", "yes", "Y", "Yes"]:
        break
    
print("Thank you!")