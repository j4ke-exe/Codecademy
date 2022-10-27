# Modules
import codecademylib3_seaborn
import random

# Define alias as plt
from matplotlib import pyplot as plt

# Set range 1 - 12
numbers_a = range(1, 13)

# Sample 12 from a range from 1 - 999
numbers_b = random.sample(range(1000), 12)

# Plot both variables
plt.show(plt.plot(numbers_a, numbers_b))
