def times3(a, b, function):
  return 3 * function(a, b)
 
add_then_times3 = times3(2, 4, lambda x, y: x + y) # 18
sub_then_times3 = times3(2, 4, lambda x, y: x - y) # -6

# -----------------------------------------
#        Review of Lambda Functions
# -----------------------------------------
# Area of a triangle: 0.5 * (base * height)
# Area of a rectangle: base * height
# Example code without using lambdas:
def rect(b, h):
  return b * h

def tri(b, h):
  return 0.5 * (b * h)

# ppsm: price per square meter
# dim: dimensions tuple
def total_cost(ppsm, dim, area):
  return ppsm * area(dim[0], dim[1])

print(total_cost(3, (5, 5), rect)) # Rectangular sheet costing 75 units
print(total_cost(4, (6, 7), tri))  # Rectangular sheet costing 84 units

# This code can be shortened by replacing the rect(b, h), and the tri(b, h) functions with lambdas.
def total_cost(ppsm, dim, area):
  return ppsm * area(dim[0], dim[1])

print(total_cost(3, (5, 5), lambda b, h: b * h))         # Rectangular sheet costing 75 units
print(total_cost(4, (6, 7), lambda b, h: 0.5 * (b * h))) # Rectangular sheet costing 84 units

# Practice 1
def odd_or_even(n, even_function, odd_function):
  if n % 2 == 0:
    return even_function(n)
  else:
    return odd_function(n)

# Checkpoint 2 code goes here.
square = lambda x: x * x
cube = lambda x: x ** 3
# Checkpoint 3 code goes here.
test = odd_or_even(5, lambda x: cube, square)
print(test)
