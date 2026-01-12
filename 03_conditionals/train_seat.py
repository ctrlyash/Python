# You're building a ticket info system for a railway app. Based on seat type, show its features.
# Task:
# • Input: "sleeper", "AC", "general", "luxury"
# • Match using match-case
# • Unknown --> show: "Invalid seat type"

seat_type = input("Enter your seat type: (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print(f"Sleeper- No AC, beds available")
    case "ac":
        print(f"AC- Air conditioned, comfy ride")
    case "general":
        print(f"General- Cheapest option, no reservation")
    case "luxury":
        print(f"Luxury- Premium seats with meals")   
    case _:
        print(f"Invalid seat type")
        
# Enter your seat type: (sleeper/AC/general/luxury): LUXURY
# Luxury- Premium seats with meals     
        

