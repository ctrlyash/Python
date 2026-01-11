# You run an online tea store. If the order amount is more than ₹300, delivery is free; otherwise, it costs 30.
# Task:
# • Input: order_amount
# • Use ternary operator to decide delivery fee

order_amount = int(input("Enter the order amount: "))

delivery_fees = 0 if order_amount > 300 else 30 # ternary operator (one-line shortcut for if-else in Python)

print(f"Delivery fee is : {delivery_fees}")

# Enter the order amount: 400
#Delivery fee is : 0