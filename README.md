# Packing Line Reject Diverter with Guard Interlocks

## Problem Statement
This project simulates a packing line reject diverter with safety features such as guard interlock, emergency stop, sensor fault detection, and manual reset. The system accepts normal packs, rejects under-weight packs, and ensures safe operation.

## Tools Used
- Python
- VS Code
- Matplotlib

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
IDLE → RUNNING → CHECK_WEIGHT → ACCEPT → STOP

---

# Task 3

## Gain Settings

### Gain Setting 1
Gain = 0.5

Observation:
- System response is slow.
- Pack checking takes more time.
- Stable operation.

### Gain Setting 2
Gain = 1.0

Observation:
- System response is normal.
- Pack checking is accurate.
- Stable operation.
- This is the selected gain because it provides a stable and accurate response.

### Gain Setting 3
Gain = 2.0

Observation:
- System response is very fast.
- May become unstable.
- Not recommended.

---

# Task 4

## Safety Features
- Emergency Stop
- Guard Interlock
- Sensor Fault Detection
- Manual Reset Required

## Test Cases
- Normal Operation
- Guard Open
- Emergency Stop
- Sensor Fault

---

# Task 5

## Test Results

| Test Case | Result | Status |
|-----------|--------|--------|
| Normal | Accept Pack | Pass |
| Low Weight | Reject Pack | Pass |
| Guard Open | Motor OFF | Pass |
| Emergency Stop | Machine Stopped | Pass |

---

# How to Run

1. Open the project in VS Code.
2. Open the terminal.
3. Run the following files one by one:

```bash
python task1.py
python task2.py
python task3.py
python task4.py
python task5.py
```

---

# Project Files

- task1.py
- task2.py
- task3.py
- task4.py
- task5.py
- README.md

---

# Conclusion

The project successfully simulates a packing line reject diverter with safety features including guard interlock, emergency stop, sensor fault detection, and manual reset. The system was tested under normal, low-weight, and fault conditions, and all tests passed successfully.