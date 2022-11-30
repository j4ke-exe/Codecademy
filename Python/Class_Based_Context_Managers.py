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
