# Inputs
guard_closed = False
emergency_stop = False
reset_button = False
weight_sensor = 97

# Check Emergency Stop
if emergency_stop:
    print("EMERGENCY STOP")
    print("Motor OFF")

# Check Guard
elif not guard_closed:
    print("Guard is Open")
    print("Motor OFF")

# Check Sensor Fault
elif weight_sensor == -1:
    print("Sensor Fault")
    print("Motor OFF")

# Normal Operation
else:
    print("Machine Running")

# Reset
if reset_button:
    print("System Reset")