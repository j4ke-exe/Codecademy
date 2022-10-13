# Define function with conditional statement
# that returns True or False based on the argument
def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False
# Prints False
print(large_power(2, 12))
# Prints True
print(large_power(2, 13))
#-------------------------------------------------
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if (food_bill + electricity_bill + internet_bill + rent > budget):
        return True
    else:
        return False
# Prints False
print(over_budget(100, 20, 30, 10, 40))
# Prints True
print(over_budget(80, 20, 30, 10, 30))
#-------------------------------------------------
def twice_as_large(num1, num2):
    if num1 > num2 * 2:
        return True
    else:
        return False
# Prints False
print(twice_as_large(10, 5))
# Prints True
print(twice_as_large(11, 5))
#-------------------------------------------------
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False
# Prints False
print(divisible_by_ten(20))
# Prints True
print(divisible_by_ten(25))
#-------------------------------------------------
def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False
# Print False
print(not_sum_to_ten(9, 1))
# Print False
print(not_sum_to_ten(5,5))
# Print True
print(not_sum_to_ten(9, -1))
