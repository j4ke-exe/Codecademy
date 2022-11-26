flight_statuses = {
  903: 'Departed',
  834: 'Boarding',
  359: 'Delayed',
  128: 'On time',
  385: 'On time',
}

print('***Small World Air Flight Information***')
for flight, status in flight_statuses.items():
  print('Flight ' + str(flight) + ' status: ' + str(status))

#--------------------------------

destinations = {
  'BUD': 'Budapest',
  'CMN': 'Casablanca',
  'IST': 'Istanbul'
}
print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'


# AssertionError handling
assert destination in destinations, 'Sorry, Small World currently does not fly to this destination!'

city_name = destinations[destination]
print('Great! Retrieving information for your flight to ...' + city_name)
