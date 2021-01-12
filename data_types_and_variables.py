little_mermaid_rental = 3
brother_bear_rental = 5
hercules_rental = 1
price_per_day = 3
rental_days= (little_mermaid_rental + brother_bear_rental + hercules_rental)
total_price = rental_days * price_per_day
print("The total price for the rentals is " + str(total_price) + " dollars. ")
#27 dollars#


#You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon
google_pay = 400
amazon_pay = 380
facebook_pay = 350
total_pay = (google_pay * 6) + (facebook_pay * 10) + (amazon_pay * 4)
print("The total pay for this week is " + str(total_pay) +  " dollars. ")

# A student can be enrolled to a class only if the class is not full 
#and the class schedule does not conflict with her current schedule. 
is_class_full = True
no_schedule_conflict = True
can_be_enrolled = is_class_full and no_schedule_conflict
print(can_be_enrolled)

#A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
#Premium members do not need to buy a specific amount of products.
buys_more_than_2 = True
offer_has_not_expired = True
is_premium_member = True
offer_can_be_applied = offer_has_not_expired and (buys_more_than_2 or is_premium_member)
print(offer_can_be_applied)

