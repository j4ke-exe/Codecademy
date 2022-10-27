drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# Iterate pairs (drinks and caffeine)
zipped_drinks = zip(drinks, caffeine)

# Dictionary comprehension to turn tuple pairs into key:value item
drinks_to_caffeine = {key: value for key, value in zipped_drinks}

print(drinks_to_caffeine)
