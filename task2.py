# Inputs
start_button = True
guard_closed = True
weight = 100

# States
state = "IDLE"

print("Current State:", state)

if start_button and guard_closed:
    state = "RUNNING"
    print("Current State:", state)

    state = "CHECK_WEIGHT"
    print("Current State:", state)

    if weight < 95:
        state = "REJECT"
    else:
        state = "ACCEPT"

    print("Current State:", state)

    state = "STOP"
    print("Current State:", state)
else:
    print("Machine Cannot Start")