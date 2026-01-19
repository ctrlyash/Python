# Generator comprehension (): It is a memory-efficient way to generate values one by one, instead of storing all values at once like a list.

# Syntax: generator = (expression for item in iterable if condition)

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = sum (sale for sale in daily_sales if sale > 5) # we can use in-built methods like filter, sum etc.
# the sum is given one by one
# It is a memory efficient operation

print(total_cups) # 61
