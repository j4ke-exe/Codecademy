# Checkpoint 1
try:
  open_file = open('file_name.txt', 'r')
  print(open_file.read())
finally:
  open_file.close()

# Checkpoint 2
with open('file_name.txt', 'r') as open_file:
  print(open_file.read())
