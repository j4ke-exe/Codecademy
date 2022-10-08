# List of stores and scoops sold
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

# Set starting point to 0
scoops_sold = 0

# Print out each store location
for location in sales_data:
  print(location)

  # Count how many scoops were sold across all stores
  for scoops in location:
    scoops_sold += scoops

# Print sum of scoops sold
print(scoops_sold)
