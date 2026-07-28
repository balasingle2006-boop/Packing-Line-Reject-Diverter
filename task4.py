import winsound

guard_closed = True
emergency_stop = False
reset_button = True
weight_sensor = 97


alarm = False


if emergency_stop:
    print("EMERGENCY STOP")
    print("Motor OFF")
    alarm = True


elif not guard_closed:
    print("Guard is Open")
    print("Motor OFF")
    alarm = True


elif weight_sensor == -1:
    print("Sensor Fault")
    print("Motor OFF")
    alarm = True


else:
    print("Machine Running")
    alarm = False


if alarm:
    print("Alarm ON")
    winsound.Beep(1000, 1000)   # 1000 Hz for 1 second
else:
    print("Alarm OFF")


if reset_button:
    print("System Reset")
    
