class Employee:
  new_id = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My ID is " + str(self.id))
  
e1 = Employee()
e2 = Employee()

e1.say_id()
e2.say_id()

#-----------------------------------

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  # Write your code below
  def say_id(self):
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()
