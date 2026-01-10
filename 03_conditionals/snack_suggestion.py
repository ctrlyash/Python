# A local cafe wants a program that suggests a snack. If a customer asks for cookies or samosa, it confirms the order. Otherwise, it says it's not available.
# Task:
# Take snack input
# If it's "cookies" or "samosa", confirm the order
# Else, show unavailability

snack = input("Enter your preffered snack: ").lower() # lower() removes case sensitivity while taking input from user ('bUrgEr' -> 'burger')


if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print(f"Sorry, we only serve cookies or samosa with tea") 
# Enter your preffered snack: cookies 
# Great Choice! We'll serve you cookies    