# You're building a smart thermostat alert system:
# If the device_status is "active"
# And temperature > 35 → Warn: "High temperature
# Else: "Temperature normal"
# If device is off → "Device is offline"

device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("Warning! High temperature")
    else:
        print("Temperature normal")
else:
    print("Device is offline")        

# Warning! High temperature    