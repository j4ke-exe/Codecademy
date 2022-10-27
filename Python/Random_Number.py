# Import module
import random

# Create random_list
random_list = [random.randint(a=0, b=100) for i in range(101)]

# Create random_number
random_number = random.choice(random_list)

# Print random_number
print(random_number)
