# Return the Next Number from the Integer Passed
# Examples
# addition(0) ➞ 1
# addition(9) ➞ 10
# addition(-3) ➞ -2

def addition(num):
    new_number = num + 1 
    return new_number

# Convert Age to Days
# calc_age(65) ➞ 23725
# calc_age(0) ➞ 0
# calc_age(20) ➞ 7300

def calc_age(age):
    calc_days = age * 365
    return calc_days

# Return the Remainder from Two Numbers
# Examples
# remainder(1, 3) ➞ 1
# remainder(3, 4) ➞ 3
# remainder(5, 5) ➞ 0
# remainder(7, 2) ➞ 1

def reminder(x, y)
    result = x % y
    return result 

# Buggy Code (Part 1)
# ans : 
def cubes(a):
	  return a ** 3

# Find the Perimeter of a Rectangle
# ans ：

def find_perimeter(length, width):
    perimeter = (length + width) * 2
    return perimeter

# To the Power of _____
# Examples
# calculate_exponent(5, 5) ➞ 3125
# calculate_exponent(10, 10) ➞ 10000000000
#calculate_exponent(3, 3) ➞ 27

def calculate_exponent(num, exp):
    result = num ** exp
    return result

calculate_exponent(3, 3)

# Football Points
# Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.
# wins get 3 points
# draws get 1 point
# losses get 0 points

def football_points(wins, draws, losses):
    final_points = wins * 3 + draws * 1 + losses * 0
    return final_points
