def convert(minutes: int) -> int: # convert minutes to seconds
    return minutes * 60


# Test cases
assert convert(1) == 60
assert convert(3) == 180
assert convert(2) == 120
assert convert(10) == 600

print("All test cases passed!")

def addition(a:int, b: int) -> int: # add two numbers
    return a + b

# Test cases
assert addition(3, 2) == 5
assert addition(-3, -6) == -9
assert addition(7, 3) == 10
assert addition(0, 0) == 0

print("All test cases passed!")

def calculate_age(age: int) -> int: # calculate age in days
    return age * 365

# Test cases
assert calculate_age(65) == 23725
assert calculate_age(0) == 0
assert calculate_age(20) == 7300
assert calculate_age(100) == 36500

print("All test cases passed!")

import math

def pythagorean(side1: int, side2: int) -> int: # calculate the hypotenuse of a right triangle
    return math.hypot(side1, side2)