# Set budget
current_budget = 3500.75

# Define variable with budget as argument
def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

# Print budget
print_remaining_budget(current_budget)

# Define variable with budget and argument to calculate expenses
def deduct_expense(budget, expense):
  return budget - expense

# Expenses
shirt_expense = 9

# Variable to calculate deducted expenses by taking current budget and subtracting expenses
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

# Print remaining budget by passing through the adjusted budget after expenses
print_remaining_budget(new_budget_after_shirt)
