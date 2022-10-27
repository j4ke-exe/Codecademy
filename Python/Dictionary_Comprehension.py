drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# Iterate pairs (drinks and caffeine)
zipped_drinks = zip(drinks, caffeine)

# Dictionary comprehension to turn tuple pairs into key:value item
drinks_to_caffeine = {key: value for key, value in zipped_drinks}

print(drinks_to_caffeine)

# ----------------------------------------------------------------

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key: value for key, value in zip(songs, playcounts)}

print(plays)

plays["Purple Haze"] = 1
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
