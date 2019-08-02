# declare string variable with value
name = "carnage kabuto"
# we get the numbers of character the string contains
name_length = len(name)  # expected: 14
# we get the first letter of the variable name: counting starts at 0
name_first_letter = name[0]  # expected: c
# we get the first 4 letters of name
name_first_four_letters = name[0:4]  # ecpected: carn
# name get the 2nd letter to 4rth letter
name_second_to_fourth = name[1:4]  # expected: arn
# name get the third to the last letter
name_third_to_last = name[2:]  # expected: rnage kabuto
# name get the first to the 5th
name_first_to_fifth = name[:5]  # expected: carna
# name get the last character
name_last_char = name[-1]  # expected o


# String Methods etc. . .
print(name.capitalize())  # to capitalize first letter
print(name.upper())  # to uppercase every leter
print(name.find("na"))

# print
print(name)
print(name_length)
print(name_first_letter)
print(name_first_four_letters)
print(name_second_to_fourth)
print(name_third_to_last)
print(name_first_to_fifth)
print(name_last_char)
