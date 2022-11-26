#Write your code below:
import itertools

max_capacity = 1000
num_bags = 0

for n in itertools.count(start=13.5, step=13.5):
  if n >= 1000:
    break
  num_bags += 1

print(num_bags)
