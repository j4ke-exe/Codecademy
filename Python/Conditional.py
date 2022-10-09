# List Comprehension: Conditional
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [n for n in heights if n > 161]
print(can_ride_coaster)
