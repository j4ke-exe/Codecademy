# Question:
# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
# Return the count of how many numbers in the list are divisible by 10.

# Solution:
def divisible_by_ten(nums):
   count = 0
   for num in nums:
      if (num % 10 == 0):
         count += 1
   return count
print(divisible_by_ten([20, 25, 30, 35, 40]))

# Output = 3

#--------------------------------------------------------

# Question:
# Create a function named add_greetings() which takes a list of strings named names as a parameter.
# In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.
# Return the new list containing the greetings.

# Solution:
def add_greetings(names):
   new_list = []
   for n in names:
      new_list.append("Hello, " + n)
   return new_list
print(add_greetings(["Owen", "Max", "Sophie"]))

# Output = ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']

#--------------------------------------------------------

# Question:
