# Concatenate first 3 letters of each name
first_name = "Jake"
last_name = "Garrison"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)

#-----------------------------------------------------

# Concatenate last 3 letters of each name
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  return first_name[-3:] + last_name[-3:]

temp_password = password_generator(first_name, last_name)

print(temp_password)
