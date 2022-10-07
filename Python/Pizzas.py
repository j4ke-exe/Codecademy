# Practicing lists, sort, pop, and append
# Pizza toppings and prices
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Calculate the number of different kinds of pizza
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# List of pizzas
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
# Sort pizzas in ascending order. Use sort(reverse=True) to set in descending order.
pizza_and_prices.sort()

# Store the first element => Cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print("Cheapest pizza: ", cheapest_pizza[-1:])

# Store the last element => Most expensive pizza
priciest_pizza = pizza_and_prices[-1]
print("Most expensive pizza: ", priciest_pizza[-1:])

# Print list of pizzas from cheapest to most expensive
print(pizza_and_prices)

# Remove most expensive pizza
pizza_and_prices.pop(-1)
print(pizza_and_prices)

# Add new topping called peppers and sort for ascending order
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)

# Slice pizza_and_prices to store the 3 cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
