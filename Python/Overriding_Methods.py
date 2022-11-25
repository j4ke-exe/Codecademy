class Animal:
  def __init__(self, name):
    self.name = name
  
  def make_noise(self):
    print("{} says, rawr.".format(self.name))

animal1 = Animal("Mia")
animal1.make_noise()
