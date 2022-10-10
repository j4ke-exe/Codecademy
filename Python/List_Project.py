# List of hairstyles
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# Price per style
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# How many sold in the previous week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Average cost 
total_price = 0
for price in prices:
  total_price += price
print("Total: " + "$" + str(total_price))

# Average haircut price
average_price = total_price / len(prices)
print("Average Haircut Price: " + "$" + str(average_price))

# Discount styles by $5
new_prices = [price - 5 for price in prices]
print("Discount Prices: " + str(list(new_prices)))

# Calculate Revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + "$" + str(total_revenue))

# Daily Average Revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: " + "$" + str(average_daily_revenue))

# Advertise haircuts that are under $30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print("Cuts under $30: " + str(cuts_under_30))
