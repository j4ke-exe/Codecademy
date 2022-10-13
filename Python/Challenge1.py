# Define function with conditional statement that returns True or False based on the argument
def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False
# Prints True
print(large_power(2, 13))
# Prints False
print(large_power(2, 12))
