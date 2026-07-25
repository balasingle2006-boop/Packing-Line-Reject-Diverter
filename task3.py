# Different weight values
weights = [100, 98, 94, 90, 101]

threshold = 95

for weight in weights:
    print("Weight:", weight)

    if weight < threshold:
        print("-> Reject Pack")
    else:
        print("-> Accept Pack")

    print("----------------")