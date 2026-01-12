# You want to simulate tea heating.
# It starts at 40°C and boils at 100°C.
# Task:
# • Use a while loop.
# • Increase temperature by 15 until it reaches or exceeds 100.
# • Print each temperature step.

temperature = 40

while temperature <= 100:
    print(f"Current temperature: {temperature}") # (If we print after adding then output will start from 55.)
    temperature += 15

print(f"Tea is ready to boil")

# Current temperature: 40
# Current temperature: 55
# Current temperature: 70
# Current temperature: 85
# Current temperature: 100
# Tea is ready to boil    