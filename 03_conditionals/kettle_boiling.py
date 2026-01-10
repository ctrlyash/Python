# You're creating a notification system for a smart kettle.
# It should remind the user only when the kettle has finished boiling Task
# A variable kettle_boiled = True
# If boiled, show: "Kettle done! Time to make chai!"

kettle_boiled = False

if kettle_boiled:
    print(f"Kettle done! Time to make chai!") # didn't print anything (condition false)


kettle_boiled = True

if kettle_boiled:
    print(f"Kettle done! Time to make chai!") # Kettle done! Time to make chai!