from functools import reduce

def lb():
  print("\n")

nums = (16, 2, 19, 22, 10, 23, 16, 2, 27, 29, 19, 26, 12, 20, 16, 29, 6, 2, 12, 20)

# Checkpoint 1 code goes here.
filtered_numbers = filter(lambda x: x % 2 == 0, nums)
print(tuple(filtered_numbers))

# Output: (16, 2, 22, 10, 16, 2, 26, 12, 20, 16, 6, 2, 12, 20)

lb() # line break

# Checkpoint 2 code goes here.
mapped_numbers = map(lambda x: x * 3, nums)
print(tuple(mapped_numbers))

# Output: (48, 6, 57, 66, 30, 69, 48, 6, 81, 87, 57, 78, 36, 60, 48, 87, 18, 6, 36, 60)

lb() # line break

# Checkpoint 3 code goes here.
sum = reduce(lambda x, y: x + y, nums)
print(sum)

# Output: 328

# -----------------------------
# Imperative Style
# -----------------------------
lst = []
for i in nums:
  if i % 3 == 0:
    lst.append(i)
 
for i in range(len(lst)):
  lst[i] = lst[i] * 3
 
tuple(lst)
# -----------------------------
# Mapping a Filtered Collection
# Declarative Style
# -----------------------------
nums = (2, 12, 5, 8, 9, 3, 16, 7, 13, 19, 21, 1, 15, 4, 22, 20, 11)

# Checkpoint 1 code goes here.
greater_than_10_doubled = map(lambda x: x * 2, filter(lambda y: y > 10, nums))

print(tuple(greater_than_10_doubled))
# Checkpoint 2 code goes here.
functional_way = map(lambda x: x * 3, filter(lambda y: y % 3 == 0, nums))

print(tuple(functional_way))
