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

#-----------------------------------------------------------

# Question:
# Create a function called win_percentage() that takes two parameters named wins and losses.
# This function should return out the total percentage of games won by a team based on these two numbers.

# Solution:
def win_percentage(wins, losses):
  return wins / (wins + losses) * 100
# Prints 50
print(win_percentage(5, 5))
# Prints 100
print(win_percentage(10, 0))

#-----------------------------------------------------------

# Question:
# Write a function named average() that has two parameters named num1 and num2.
# The function should return the average of these two numbers.

# Solution:
def average(num1, num2):
  return (num1 + num2) / 2
# The average of 1 and 100 is 50.5
print(average(1, 100))
# The average of 1 and -1 is 0
print(average(1, -1))

#-----------------------------------------------------------

# Question:
# Write a function named remainder() that has two parameters named num1 and num2.
# The function should return the remainder of twice num1 divided by half of num2.

# Solution:
def remainder(num1, num2):
  return (num1 * 2) % (num2 / 2)
# Prints 2.0
print(remainder(15, 14))
# Prints 0.0
print(remainder(9, 6))
