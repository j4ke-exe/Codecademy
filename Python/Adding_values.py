num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

# Count the num of exercises in num_exercises
# by using the .values() method to gather the sum
# and add it to the total_exercises variable.
for num in num_exercises.values():
  total_exercises += num
print(total_exercises)
