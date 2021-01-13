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

