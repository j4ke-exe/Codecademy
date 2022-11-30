# Write your code below: 
class PoemFiles:
  
  def __init__(self):
    print("Creating Poems!")
  
  def __enter__(self):
    print("Opening poem file")
  
  def __exit__(self, *exc):
    print("Closing poem file")

with PoemFiles() as manager:
  print("Hope is the thing with feathers")

#----------------------------
# Class Based Context Managers II

# Write your code below:
class PoemFiles:

  def __init__(self, poem_file, mode):
    print("Starting up a poem context manager")
    self.file = poem_file
    self.mode = mode
  
  def __enter__(self):
    print("Opening poem file")
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file
  
  def __exit__(self, *exc):
    print("Closing poem file")
    return self.opened_poem_file.close()

with PoemFiles('poem.txt', 'w') as open_poem_file:
  open_poem_file.write('Hope is the thing with feathers')

#----------------------------
# Handling Exceptions I

class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n ')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  # Create your __exit__ method here:
  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type, exc_value, traceback)
    return self.opened_poem_file.close()

# First (Throws Error)
# with PoemFiles('poem.txt', 'r') as file:
#   print("---- Exception data below ----")
#   print(file.uppercasewords())

# Second (Handles Error)
with PoemFiles('poem.txt', 'r') as file2:
   print(file2.read())
   print("---- Exception data below ----")

#---------------------------
# Handling Exceptions II

class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print(' \n --  Opening poem file -- \n')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type, exc_value, traceback, '\n')
    # Write your code below: 
    if isinstance(exc_value, AttributeError):
      self.opened_poem_file.close()
      return True

with PoemFiles('poem.txt', 'r') as file:
  print("---- Exception data below ---- \n ")
  print(file.uppercasewords())

with PoemFiles('poem.txt', 'r') as file2:
  print(file2.read())
  print(" \n ---- Exception data below ---- \n ")
