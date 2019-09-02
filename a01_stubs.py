######################################################################
# Author: Dr. Scott Heggen      TODO: Sama Manalai
# Username: heggens             TODO: manalais
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
user_birthday = input('What is your date of birth? ')
# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples
if user_birthday == '1998':
    print('You are a tiger')
elif user_birthday == '1999':
    print('You are a Rabbit!')
elif user_birthday == '2000':
    print('You are a Dragon')
elif user_birthday == '2001':
    print('You are a Snake')
elif user_birthday == '2002':
    print('You are a Horse')
elif user_birthday == '2003':
    print('You are a Goat')
elif user_birthday == '2004':
    print('You are a Monkey')
elif user_birthday == '2005':
    print('You are a Rooster')
elif user_birthday == '2006':
    print('You are a Dog')
elif user_birthday == '2007':
    print('You are a Pig')
elif user_birthday == '2008':
    print('You are a Rat')
elif user_birthday == '2009':
    print('You are an Ox')


    ######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year
friend_birthday = input("What is your friend's date of birth? ")

# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year
if friend_birthday == '1998':
    print('Your friend is a tiger')
elif friend_birthday == '1999':
    print('Your friend is a Rabbit!')
elif friend_birthday == '2000':
    print('Your friend is a Dragon')
elif friend_birthday == '2001':
    print('Your friend is a Snake')
elif friend_birthday == '2002':
    print('Your friend is a Horse')
elif friend_birthday == '2003':
    print('Your friend is a Goat')
elif friend_birthday == '2004':
    print('Your friend is a Monkey')
elif friend_birthday == '2005':
    print('Your friend is a Rooster')
elif friend_birthday == '2006':
    print('Your friend is a Dog')
elif friend_birthday == '2007':
    print('Your friend is a Pig')
elif friend_birthday == '2008':
    print('Your friend is a Rat')
elif friend_birthday == '2009':
    print('Your friend is an Ox')


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
