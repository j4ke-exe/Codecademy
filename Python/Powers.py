# Powers
single_digits = range(10)
squares = []

for digit in single_digits:
  print(digit)
  # Each element of digit taken to second power from single_digits
  squares.append(digit**2)
  
print(squares)

# Each element of cubes taken to third power from single_digits
cubes = [cube**3 for cube in single_digits]
print(cubes)
