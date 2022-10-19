first_name = "Jake"
last_name = "Garrison"

def account_generator(first_name, last_name):
  # Concatenate first 3 letters of each name
  account_name = first_name[:3] + last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)
