# Calculate force

train_mass = 22680
train_acceleration = 10
def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

bomb_mass = 1
def get_energy(mass, c=3*10**8):
  return mass * c^2
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

train_distance = 100
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration)
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
