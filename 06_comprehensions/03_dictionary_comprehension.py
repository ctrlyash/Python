# Dictionary comprehension: It is a short and clean way to create a dictionary using one line of code.

# Syntax: new_dict = {key:value for item in iterable} # expression in dictionary comprehension is key:value pair

tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}


tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()} # here the returning values form key:value pair and we can also perform any of our desired operation in expression.

print(tea_prices_usd) # {'Masala Chai': 0.5, 'Green Tea': 0.625, 'Lemon Tea': 2.5}
