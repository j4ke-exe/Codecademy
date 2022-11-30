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
