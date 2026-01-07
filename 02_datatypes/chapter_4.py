import sys
from decimal import Decimal # do exist in python
from fractions import Fraction # do exist in python as complex numbers ( none of our use as of now)


# Real Number: In Python, a real number is represented using the float type, which stores decimal values as binary floating-point numbers (IEEE-754).

# Example of Floating point numbers
ideal_temp = 95.5
current_temp = 95.49999999999999999999999999

print(f"Ideal temp {ideal_temp}") # Ideal temp 95.5

print(f"Current temp {current_temp}") # Current temp 95.5 
# Python rounded up current_temp to 95.5
# Because Python stores numbers in binary floating-point (IEEE-754), it cannot represent extremely precise decimals exactly, so it rounds them to the nearest representable value.

print(f"Difference temp {ideal_temp - current_temp}") # Difference temp 0.0


print(sys.float_info) # sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1) *Varies from system to system.