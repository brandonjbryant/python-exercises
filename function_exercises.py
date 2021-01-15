# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    return  x == '2' or x == 2



# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(letter):
    return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this. 
def is_consonant(letter):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return len(letter) == 1 and letter.isalpha() and not is_vowel(letter)
is_consonant('b')

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalized_consonant(word):
    first_letter = word[0]
    if is_consonant(first_letter):
        return word.capitalize()
    else:
        return word

assert capitalized_consonant('mac') == 'Mac'
assert capitalized_consonant('codeup') == 'Codeup'

print("Exercise is correct.")
# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip_percentage,bill_total):
    amount_to_tip = tip_percentage * bill_total
    return amount_to_tip

assert calculate_tip(.5,13.50)
assert calculate_tip(.25,20)

print("Exercise is correct")

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price,discount):
    discounted_price = original_price * discount
    return original_price - discounted_price

assert apply_discount(15,.5)
assert apply_discount(52,.16)

print("Exercise is correct")

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(numeric_string):
    number_without_commas = numeric_string.replace(',', '')
    real_number = int(number_without_commas)
    return real_number

assert handle_commas('1,234') == 1234
assert handle_commas('1,234,567') == 1234567
assert handle_commas('123') == 123


print("Exercise is correct")
# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(numeric_grade):
    if numeric_grade >= 90:
        return 'A'
    elif numeric_grade >= 80:
        return 'B'
    elif numeric_grade >= 70:
        return 'C'
    else:
        return 'F'

assert get_letter_grade(90) == 'A'
assert get_letter_grade(95) == 'A'
assert get_letter_grade(80) == 'B'
assert get_letter_grade(85) == 'B'
assert get_letter_grade(70) == 'C'
assert get_letter_grade(60) == 'F'

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
 #A. anything that is not a valid python identifier should be removed
 #B. leading and trailing whitespace should be removed
 #C. everything should be lowercase
 #D. spaces should be replaced with underscores
    ##for example:
#Name will become name
#First Name will become first_name
#% Completed will become completed 

#Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
 #cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    #cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]