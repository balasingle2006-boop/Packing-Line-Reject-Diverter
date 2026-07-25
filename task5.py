# Test Cases

test_cases = [
    {"name": "Normal", "weight": 100, "guard": True, "emergency": False},
    {"name": "Low Weight", "weight": 90, "guard": True, "emergency": False},
    {"name": "Guard Open", "weight": 100, "guard": False, "emergency": False},
    {"name": "Emergency Stop", "weight": 100, "guard": True, "emergency": True},
]

for test in test_cases:
    print("\n-----", test["name"], "-----")

    if test["emergency"]:
        print("Result: Emergency Stop")
    elif not test["guard"]:
        print("Result: Guard Open - Motor OFF")
    elif test["weight"] < 95:
        print("Result: Reject Pack")
    else:
        print("Result: Accept Pack")