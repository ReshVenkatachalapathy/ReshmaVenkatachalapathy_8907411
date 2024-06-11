#Project Name: pythagorean_theorem
#Developer: Reshma
#Description: This task will calculate the pythagoras theorem

import math

#Get the altitude and base side values of the triangle. Calculate using the formula a^2 + b^2.
def trianglesides(rightside, leftside):
    return (rightside*rightside) + (leftside*leftside)

# Calculate the hypotenuse value by finding the square root of the triangle sides
def hypotenuse(sides):
    return math.sqrt(sides)