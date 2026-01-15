# Improving traceability

# You shop adds a 10% VAT on every order.
# You want this to be consistent and traceable.
# Task:
# - Write add_vat(price, vat_rate)
# - Use it to compute final prices for 3 orders


def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 100)
    print(f"Original: {price}, Final with VAT: {final_amount} ")

# Original: 100, Final with VAT: 200.0 
# Original: 150, Final with VAT: 300.0 
# Original: 200, Final with VAT: 400.0 