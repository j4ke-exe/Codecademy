instrument_catalog = {
  'Marimba': 1999,
  'Kora': 499,
  'Flute': 899
}

def print_instrument_price(instrument):
  if instrument in instrument_catalog:
    print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))
  else:
    raise KeyError(instrument + " is not found in instrument catalog!")

print_instrument_price('Marimba')
print_instrument_price('Flute')
print_instrument_price('Piano')

#---------------------------------

staff = {
  'Austin': {
      'floor managers': 1,
      'sales associates': 5
  },
  'Melbourne': {
      'floor managers': 0,
      'sales associates': 8
  },
  'Beijing': {
      'floor managers': 2,
      'sales associates': 5
  },
}

def print_staff_report(location, staff_dict):
  managers = staff_dict['floor managers']
  sales_people = staff_dict['sales associates']
  ratio = sales_people / managers
  print('Instrument World ' + location + ' has:')
  print(str(sales_people) + ' sales employees')
  print(str(managers) + ' floor managers')
  print('The ratio of sales people to managers is ' + str(ratio))
  print()

for location, staff in staff.items():
  # Write your code below:
  try:
    print_staff_report(location, staff)
  except:
    print("*** Could not print sales report for " + location + " ***" + "\n")

#-------------------------------

staff = {
  'Austin': {
    'floor managers': 1,
    'sales associates': 5
  },
  'Melbourne': {
    'floor managers': 0,
    'sales associates': 8
  },
  'Beijing': {
    'floor managers': 2,
    'sales associates': 5
  },
}

def print_staff_report(location, staff_dict):
  managers = staff_dict['floor managers']
  sales_people = staff_dict['sales associates']
  ratio = sales_people / managers
  print('Instrument World ' + location + ' has:')
  print(str(sales_people) + ' sales employees')
  print(str(managers) + ' floor managers')
  print('The ratio of sales people to managers is ' + str(ratio))
  print()

for location, staff in staff.items():
  try:
      print_staff_report(location, staff)
  except ZeroDivisionError as e:
      print('Could not print sales report for ' + location + "\n")
      print(str(e) + "\n")

#-------------------------------

instrument_prices = {
  'Banjo': 200,
  'Cello': 1000,
  'Flute': 100,
}

def display_discounted_price(instrument, discount):
  full_price = instrument_prices[instrument]
  discount_percentage = discount / 100
  discounted_price = full_price - (full_price * discount_percentage)
  print("The instrument's discounted price is: " + str(discounted_price))

instrument = 'Banjo'
discount = 20

# Write your code below:
try:
  display_discounted_price(instrument, discount)
except KeyError:
  print("An invalid instrument was entered!")
except TypeError:
  print("Discount percentage must be a number!")
except Exception:
  print("Hit an exception other than KeyError or TypeError!")

#------------------------------

customer_rewards = {
  'Zoltan': 82570,
  'Guadalupe': 29850,
  'Mario': 17849
}

def display_rewards_account(customer):
  try:
    rewards_number = customer_rewards[customer]
  except KeyError:
    print("Customer was not found in rewards program!")
  else:
    print('Rewards account number is: ' + str(rewards_number))

customer = 'Mario'
display_rewards_account(customer)

#--------------------------------
# Try, Except, Else, and Finally statements

import database

instrument = 'Kora'
database.connect_to_database()

try:
  database.display_instrument_info(instrument)
except KeyError:
  print('Oh no! This instrument does not exist.')
else:
  print(instrument)
# Write your code below: 
finally:
  database.disconnect_from_database()
