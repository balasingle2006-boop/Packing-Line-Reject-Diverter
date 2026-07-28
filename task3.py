
weights = [100, 98, 94, 90, 101]

threshold = 95


gain = 1.0

print("Gain:", gain)
print("----------------")

for weight in weights:

    
    adjusted_weight = weight * gain

    print("Original Weight:", weight)
    print("Adjusted Weight:", adjusted_weight)

    if adjusted_weight < threshold:
        print("-> Reject Pack")
    else:
        print("-> Accept Pack")

    print("----------------")
