# Hiding Implementation details

# You're building a simple app that registers users.
# You want to separate concerns: getting input, validating it, saving it.
# Task:
# Write register_user() that calls:
# - get_input()
# - validate_input()
# - save_to_db()


def get_input():
    print("Getting user input")


def validate_input():
    print("validating the user info")    


def save_to_db():
    print("Saving to database")


def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registration is complete!")    


register_user()

# Getting user input
# validating the user info
# Saving to database
# User registration is complete!