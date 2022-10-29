class Circle:
  pi = 3.14
  
  # Add constructor
  def __init__(self, diameter):
    print("New circle with diameter: {}".format(diameter))

teach_table = Circle(36)

#---------------------------------------------------------

class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"
