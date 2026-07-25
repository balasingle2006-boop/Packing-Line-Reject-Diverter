# Packing Line Reject Diverter with Guard Interlocks

## Student Details
- **Name:** BALA VIGNESH.S
- **Register Number:** 411724106005
- **Department:** Electronics and Communication Engineering (ECE)
- **College:** PSVPEC

---

# Problem Statement

This project simulates a Packing Line Reject Diverter with Guard Interlocks. The system checks the weight of each pack and automatically rejects under-weight packs. It also provides safety features such as Guard Interlock, Emergency Stop, Sensor Fault Detection, and Manual Reset to ensure safe operation.

---

# Objective

- To identify under-weight packs.
- To reject defective packs automatically.
- To prevent unsafe machine operation.
- To stop the machine immediately during emergency conditions.
- To allow restart only after manual reset.

---

# Tools Used

- Python
- Visual Studio Code (VS Code)
- Matplotlib

---

# Project Files

- task1.py
- task2.py
- task3.py
- task4.py
- task5.py
- README.md

---

# Task 1

## Requirements

- Sampling Interval: 1 second
- Safe Weight Range: 95–105 g
- Reject Threshold: Below 95 g
- Consecutive Readings Required: 3

## Test Signals

- Normal Signal
- Low Weight Signal
- Noisy Signal

---

# Task 2

## Inputs

- Start Button
- Guard Sensor
- Weight Sensor

## Outputs

- Motor
- Diverter
- Alarm

## States

- IDLE
- RUNNING
- CHECK_WEIGHT
- ACCEPT
- REJECT
- STOP

## Unsafe Situations

1. Motor should not run when the guard is open.
2. Under-weight packs should not be accepted.
3. The machine should not restart automatically after an emergency stop.

## Normal State Sequence

```
IDLE
   ↓
RUNNING
   ↓
CHECK_WEIGHT
   ↓
ACCEPT / REJECT
   ↓
STOP
```

---

# Task 3

## Gain Settings

### Gain = 0.5

Observation:

- Slow response
- Stable operation
- Takes more time to process

### Gain = 1.0

Observation:

- Normal response
- Stable operation
- Accurate pack checking
- **Selected Gain**

### Gain = 2.0

Observation:

- Very fast response
- May become unstable
- Not recommended

---

# Task 4

## Safety Features

- Emergency Stop
- Guard Interlock
- Sensor Fault Detection
- Manual Reset

## Test Cases

| Test Case | Result |
|-----------|--------|
| Normal Operation | Machine Running |
| Guard Open | Motor OFF |
| Emergency Stop | Machine Stopped |
| Sensor Fault | Motor OFF |

---

# Task 5

## Final Test Results

| Test Case | Expected Result | Status |
|-----------|-----------------|--------|
| Normal | Accept Pack | Pass |
| Low Weight | Reject Pack | Pass |
| Guard Open | Motor OFF | Pass |
| Emergency Stop | Machine Stopped | Pass |

---

# How to Run the Project

1. Open the project in VS Code.
2. Open the Terminal.
3. Run the following commands one by one.

```bash
python task1.py
python task2.py
python task3.py
python task4.py
python task5.py
```

---

# Expected Output

- Normal weight → Accept Pack
- Weight below 95 g → Reject Pack
- Guard Open → Motor OFF
- Emergency Stop → Machine Stopped
- Sensor Fault → Motor OFF

---

# Safety Features Implemented

- Automatic Reject System
- Guard Interlock
- Emergency Stop
- Sensor Fault Detection
- Manual Reset

---

# Conclusion

This project successfully simulates a Packing Line Reject Diverter with Guard Interlocks using Python. The system correctly accepts normal packs, rejects under-weight packs, detects unsafe conditions, and stops the machine whenever required. All required tasks were completed and tested successfully.

---

# Future Improvements

- Real-time sensor integration
- PLC implementation
- IoT monitoring
- Automatic data logging
- Industrial HMI interface
