from helper_functions import process_csv_supplies
from collections import deque

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Write your code below!
supplies_deque = deque()
for item in csv_data:
  if item[2] == 'important':
    supplies_deque.appendleft(item)
  else:
    supplies_deque.append(item)

ordered_important_supplies = deque()
for order in range(25):
  ordered_important_supplies.append(supplies_deque.popleft())

ordered_unimportant_supplies = deque()
for order in range(10):
  ordered_unimportant_supplies.append(supplies_deque.pop())

print(supplies_deque, "\n")
print(ordered_important_supplies, "\n")
print(ordered_unimportant_supplies)
