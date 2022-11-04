class Cat:
  def __init__(self, input_name, input_breed, input_age = 0):
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_cuddly = True

  def have_birthday(self):
    self.age = self.age + 1
    print("{name} had a birthday! {name} is {age} years old.".format(name = self.name, age = self.age))

new_cat = Cat("Mia", "Bengal", 3)

new_cat.have_birthday()
