# Circle or Square
# Given the radius of a circle and the area of a square, return True if the circumference of the circle is greater than the square's perimeter and False if the square's perimeter is greater than the circumference of the circle.
# Examples  circle_or_square(16, 625) ➞ True

def circle_or_square(rad, area):
    import math
    side_length = math.sqrt(area)
    pi = float(3.14)
    rad_circumference = float(rad * 2 * pi)
    square_perimeter = 4 * side_length 
    if rad_circumference > square_perimeter:
    	return True
    else:
   		return False 
