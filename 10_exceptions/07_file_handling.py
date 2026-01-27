# File handling in Python: Opening, writing, and closing files


file = open("order.txt", "w")
file.write("Masala Chai- 2 cups")
file.close()

# order.txt file is created with the content "Masala Chai- 2 cups"

# this type of file handling is not recommended
# because if any exception occurs between open and close, the file will not be closed properly and may lead to data loss or corruption.

# better way of file handling using try and finally
#(also not recommended)

file = open("order2.txt", "w")
try:
    file.write("Masala Chai- 2 cups")
finally:
    file.close()

# order2.txt file is created with the content "Masala Chai- 2 cups"    


# recommended way of file handling using 'with' statement
with open("order3.txt", "w") as file:
    file.write("Masala Chai- 2 cups")

# order3.txt file is created with the content "Masala Chai- 2 cups"    

