import itertools

collars = ["Red-S", "Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

collar_combo_iterator = itertools.combinations(collars, 3)
for i in collar_combo_iterator:
  print(i)
