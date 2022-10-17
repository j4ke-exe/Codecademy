# Question:
# Write a function named tenth_power() that has one parameter named num.
# The function should return num raised to the 10th power.

# Solution:
def tenth_power(num):
  return num ** 10
# 1 to the 10th power is 1
print(tenth_power(1))
# 0 to the 10th power is 0
print(tenth_power(0))
# 2 to the 10th power is 1024
print(tenth_power(2))

# Output = 1, 0, 1024

#-----------------------------------------------------------

# Question:
# Write a function named square_root() that has one parameter named num.
# Use exponents (**) to return the square root of num.

# Solution:
def square_root(num):
  return num ** .5
# should print 4
print(square_root(16))
# should print 10
print(square_root(100))

# Output = 4.0, 10.0
