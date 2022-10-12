# Example of a global scope function
balance = 100.25
name = "Jake"

def withdraw_money(amount):
  result = balance - amount
  print("Hello " + name + " your balance remaining is: $" + str(result))
  return amount

withdraw_money(25)
print("Save your money " + name + "!")
