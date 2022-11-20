def total_bill(func, value):
  total = func(value)
  return ("The total amount owed is $" + "{:.2f}".format(total))
 
print(total_bill(add_tax, 100))
print(total_bill(add_tip, 100))
