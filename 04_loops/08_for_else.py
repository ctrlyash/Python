# for else loop example-

staff = [("Amit",16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break # (breaks the loop i.e. no more iteration)
else:
    print(f"No one is eligible to manage the staff") #  (else block in for else only executes if the loop doesnt breaks)

 # Amit is eligible to manage the staff   