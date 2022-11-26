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
